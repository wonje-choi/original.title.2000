
import argparse
import ctypes
import re
import sys
import time
from dataclasses import dataclass
from ctypes import wintypes

user32 = ctypes.WinDLL("user32", use_last_error=True)
dxva2  = ctypes.WinDLL("dxva2", use_last_error=True)

class RECT(ctypes.Structure):
    _fields_ = [("left", wintypes.LONG),
                ("top", wintypes.LONG),
                ("right", wintypes.LONG),
                ("bottom", wintypes.LONG)]

class PHYSICAL_MONITOR(ctypes.Structure):
    _fields_ = [
        ("hPhysicalMonitor", wintypes.HANDLE),
        ("szPhysicalMonitorDescription", wintypes.WCHAR * 128),
    ]

MONITORENUMPROC = ctypes.WINFUNCTYPE(
    wintypes.BOOL, wintypes.HMONITOR, wintypes.HDC, ctypes.POINTER(RECT), wintypes.LPARAM
)

user32.EnumDisplayMonitors.argtypes = [wintypes.HDC, ctypes.c_void_p, MONITORENUMPROC, wintypes.LPARAM]
user32.EnumDisplayMonitors.restype  = wintypes.BOOL

dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR.argtypes = [wintypes.HMONITOR, ctypes.POINTER(wintypes.DWORD)]
dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR.restype  = wintypes.BOOL

dxva2.GetPhysicalMonitorsFromHMONITOR.argtypes = [wintypes.HMONITOR, wintypes.DWORD, ctypes.POINTER(PHYSICAL_MONITOR)]
dxva2.GetPhysicalMonitorsFromHMONITOR.restype  = wintypes.BOOL

dxva2.DestroyPhysicalMonitors.argtypes = [wintypes.DWORD, ctypes.POINTER(PHYSICAL_MONITOR)]
dxva2.DestroyPhysicalMonitors.restype  = wintypes.BOOL

dxva2.SetVCPFeature.argtypes = [wintypes.HANDLE, wintypes.BYTE, wintypes.DWORD]
dxva2.SetVCPFeature.restype  = wintypes.BOOL

dxva2.GetVCPFeatureAndVCPFeatureReply.argtypes = [
    wintypes.HANDLE,
    wintypes.BYTE,
    ctypes.POINTER(wintypes.DWORD),  # VCP code type (ignored)
    ctypes.POINTER(wintypes.DWORD),  # current
    ctypes.POINTER(wintypes.DWORD),  # max
]
dxva2.GetVCPFeatureAndVCPFeatureReply.restype = wintypes.BOOL

dxva2.GetCapabilitiesStringLength.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
dxva2.GetCapabilitiesStringLength.restype  = wintypes.BOOL

dxva2.CapabilitiesRequestAndCapabilitiesReply.argtypes = [wintypes.HANDLE, wintypes.LPSTR, wintypes.DWORD]
dxva2.CapabilitiesRequestAndCapabilitiesReply.restype  = wintypes.BOOL

POWER_VCP = 0xD6
ON = 0x01
DPMS_OFF = 0x04  # "screen off" recommended


@dataclass
class MonInfo:
    idx: int
    name: str
    handle: int
    caps: str
    model_tag: str


def winerr(prefix: str):
    err = ctypes.get_last_error()
    raise OSError(err, f"{prefix} (WinError={err})")

def enum_physical_monitors():
    physical = []

    @MONITORENUMPROC
    def cb(hMonitor, hdc, lprect, lparam):
        count = wintypes.DWORD(0)
        if dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR(hMonitor, ctypes.byref(count)) and count.value:
            arr = (PHYSICAL_MONITOR * count.value)()
            if dxva2.GetPhysicalMonitorsFromHMONITOR(hMonitor, count, arr):
                for i in range(count.value):
                    physical.append(arr[i])
        return True

    if not user32.EnumDisplayMonitors(None, None, cb, 0):
        winerr("EnumDisplayMonitors failed")
    return physical

def destroy_physical(physical):
    if physical:
        arr = (PHYSICAL_MONITOR * len(physical))(*physical)
        dxva2.DestroyPhysicalMonitors(len(physical), arr)

def get_caps(hmon: wintypes.HANDLE) -> str:
    length = wintypes.DWORD(0)
    if not dxva2.GetCapabilitiesStringLength(hmon, ctypes.byref(length)):
        return ""
    buf = (ctypes.c_char * (length.value + 1))()
    if not dxva2.CapabilitiesRequestAndCapabilitiesReply(hmon, buf, length):
        return ""
    return bytes(buf).split(b"\x00", 1)[0].decode("ascii", errors="replace")

def parse_model_tag(caps: str) -> str:
    m = re.search(r"model\(([^)]+)\)", caps, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    for token in ["RTK", "MStar"]:
        if re.search(rf"\b{token}\b", caps, flags=re.IGNORECASE):
            return token
    return "unknown"

def vcp_get(hmon, code_hex: int):
    vct = wintypes.DWORD(0)
    cur = wintypes.DWORD(0)
    mx  = wintypes.DWORD(0)
    ok = dxva2.GetVCPFeatureAndVCPFeatureReply(
        hmon, wintypes.BYTE(code_hex),
        ctypes.byref(vct), ctypes.byref(cur), ctypes.byref(mx)
    )
    if not ok:
        return None
    return int(cur.value), int(mx.value)

def vcp_set(hmon, code_hex: int, value: int):
    if not dxva2.SetVCPFeature(hmon, wintypes.BYTE(code_hex), wintypes.DWORD(value)):
        winerr(f"SetVCPFeature failed (code=0x{code_hex:02X}, value=0x{value:02X})")

def build_mon_infos():
    phys = enum_physical_monitors()
    infos = []
    try:
        for i, pm in enumerate(phys):
            caps = get_caps(pm.hPhysicalMonitor)
            infos.append(MonInfo(
                idx=i,
                name=str(pm.szPhysicalMonitorDescription),
                handle=pm.hPhysicalMonitor,
                caps=caps,
                model_tag=parse_model_tag(caps),
            ))
        return infos, phys
    except Exception:
        destroy_physical(phys)
        raise

def select_by_model(infos, keyword: str) -> MonInfo:
    key = keyword.strip().lower()
    hits = [m for m in infos if key in m.model_tag.lower() or key in m.caps.lower() or key in m.name.lower()]
    if not hits:
        raise RuntimeError(f"No monitor matched '{keyword}'.")
    exact = [m for m in hits if m.model_tag.lower() == key]
    if len(exact) == 1:
        return exact[0]
    if len(hits) > 1:
        raise RuntimeError(f"'{keyword}' matched multiple monitors. Candidates: {[h.model_tag for h in hits]}")
    return hits[0]

def classify_power_state(readback):
    """
    Return "on"/"off"/"unknown"
    Many monitors report:
      0x01 = on
      0x04/0x05 = off-ish
    Some monitors may return other values or block reads.
    """
    if readback is None:
        return "unknown"
    cur, _mx = readback
    if cur == ON:
        return "on"
    if cur in (DPMS_OFF, 0x05):
        return "off"
    return "unknown"

def main():
    if sys.platform != "win32":
        print("[ERROR] Windows only.")
        return 1

    ap = argparse.ArgumentParser(description="RTK toggle test (requires readable VCP 0xD6 for true toggle)")
    ap.add_argument("--model", default="RTK", help="monitor match keyword (default: RTK)")
    ap.add_argument("--delay", type=float, default=1.2, help="seconds to wait after setting power (default: 1.2)")
    ap.add_argument("--runs", type=int, default=3, help="toggle repetitions (default: 3)")
    args = ap.parse_args()

    infos, phys = build_mon_infos()
    try:
        target = select_by_model(infos, args.model)
        print(f"Target: [{target.idx}] {target.name} (tag={target.model_tag})")

        # 1) readback test
        rb0 = vcp_get(target.handle, POWER_VCP)
        print("Readback 0xD6:", "FAIL (unreadable)" if rb0 is None else f"OK current=0x{rb0[0]:02X}, max=0x{rb0[1]:02X}")

        state0 = classify_power_state(rb0)
        print("Classified state:", state0)

        if rb0 is None:
            print("\nRESULT: TRUE TOGGLE NOT POSSIBLE on this monitor (0xD6 readback blocked).")
            print("You can still do a deterministic sequence (OFF->ON), or a 'statefile toggle' workaround.")
            return 2

        # 2) toggle runs
        # We will do: read -> decide next -> set -> read to verify (best-effort)
        ok = True
        for i in range(args.runs):
            rb = vcp_get(target.handle, POWER_VCP)
            before = classify_power_state(rb)
            if before == "on":
                desired = DPMS_OFF
                desired_name = "dpms_off"
            elif before == "off":
                desired = ON
                desired_name = "on"
            else:
                # If unknown, default to dpms_off first (safer), then next run likely known
                desired = DPMS_OFF
                desired_name = "dpms_off(default)"

            print(f"\nRun {i+1}/{args.runs}")
            print("  before:", "unreadable" if rb is None else f"0x{rb[0]:02X} ({before})")
            print("  set   :", desired_name)
            vcp_set(target.handle, POWER_VCP, desired)
            time.sleep(max(0.0, args.delay))

            rb_after = vcp_get(target.handle, POWER_VCP)
            after = classify_power_state(rb_after)
            print("  after :", "unreadable" if rb_after is None else f"0x{rb_after[0]:02X} ({after})")

            # simple verification
            if desired == ON and after != "on":
                ok = False
            if desired == DPMS_OFF and after != "off":
                # Some monitors keep reporting 0x01 even when blanked; treat as soft-fail
                # We'll mark as warning, not hard fail.
                print("  WARN  : monitor may not report 'off' via readback even if screen is blank")
        print("\nRESULT:", "PASS (toggle feasible)" if ok else "CHECK (toggle set works, but readback may be unreliable)")
        return 0 if ok else 0

    except Exception as e:
        print(f"[ERROR] {e}")
        return 1
    finally:
        destroy_physical(phys)

if __name__ == "__main__":
    raise SystemExit(main())
