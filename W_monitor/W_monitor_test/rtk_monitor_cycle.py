
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
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]

class PHYSICAL_MONITOR(ctypes.Structure):
    _fields_ = [
        ("hPhysicalMonitor", wintypes.HANDLE),
        ("szPhysicalMonitorDescription", wintypes.WCHAR * 128),
    ]

MONITORENUMPROC = ctypes.WINFUNCTYPE(
    wintypes.BOOL,
    wintypes.HMONITOR,
    wintypes.HDC,
    ctypes.POINTER(RECT),
    wintypes.LPARAM,
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

dxva2.GetCapabilitiesStringLength.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
dxva2.GetCapabilitiesStringLength.restype  = wintypes.BOOL

dxva2.CapabilitiesRequestAndCapabilitiesReply.argtypes = [wintypes.HANDLE, wintypes.LPSTR, wintypes.DWORD]
dxva2.CapabilitiesRequestAndCapabilitiesReply.restype  = wintypes.BOOL


POWER_VCP = 0xD6
POWER_ON = 0x01
POWER_DPMS_OFF = 0x04  # recommended for "screen off"


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
    # Prefer exact model_tag match if multiple
    exact = [m for m in hits if m.model_tag.lower() == key]
    if len(exact) == 1:
        return exact[0]
    if len(hits) > 1:
        raise RuntimeError(f"'{keyword}' matched multiple monitors. Candidates: {[h.model_tag for h in hits]}")
    return hits[0]

def main():
    if sys.platform != "win32":
        print("[ERROR] Windows only.")
        return 1

    ap = argparse.ArgumentParser(description="Cycle RTK monitor: dpms_off -> wait -> on")
    ap.add_argument("--model", default="RTK", help="monitor match keyword (default: RTK)")
    ap.add_argument("--delay", type=float, default=2.0, help="seconds to wait between off and on (default: 2.0)")
    ap.add_argument("--repeat", type=int, default=1, help="how many cycles to run (default: 1)")
    args = ap.parse_args()

    infos, phys = build_mon_infos()
    try:
        target = select_by_model(infos, args.model)
        print(f"Target: [{target.idx}] {target.name} (tag={target.model_tag})")

        for n in range(args.repeat):
            print(f"Cycle {n+1}/{args.repeat}: OFF (dpms_off)")
            vcp_set(target.handle, POWER_VCP, POWER_DPMS_OFF)

            time.sleep(max(0.0, args.delay))

            print(f"Cycle {n+1}/{args.repeat}: ON")
            vcp_set(target.handle, POWER_VCP, POWER_ON)

            # small settle time between repeats
            time.sleep(0.2)

        print("DONE")
        return 0

    except Exception as e:
        print(f"[ERROR] {e}")
        return 1
    finally:
        destroy_physical(phys)

if __name__ == "__main__":
    raise SystemExit(main())
