import argparse
import ctypes
import re
import sys
import time
from dataclasses import dataclass
from ctypes import wintypes

user32 = ctypes.WinDLL("user32", use_last_error=True)
dxva2  = ctypes.WinDLL("dxva2", use_last_error=True)

# -------------------- Win32 structs --------------------
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
    wintypes.BOOL,
    wintypes.HMONITOR,
    wintypes.HDC,
    ctypes.POINTER(RECT),
    wintypes.LPARAM
)

# -------------------- Prototypes --------------------
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
    wintypes.HANDLE,           # hMonitor
    wintypes.BYTE,             # bVCPCode
    ctypes.POINTER(wintypes.DWORD),  # pvct (MC_VCP_CODE_TYPE) - we treat as DWORD
    ctypes.POINTER(wintypes.DWORD),  # pdwCurrentValue
    ctypes.POINTER(wintypes.DWORD),  # pdwMaximumValue
]
dxva2.GetVCPFeatureAndVCPFeatureReply.restype = wintypes.BOOL

dxva2.GetCapabilitiesStringLength.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
dxva2.GetCapabilitiesStringLength.restype  = wintypes.BOOL

dxva2.CapabilitiesRequestAndCapabilitiesReply.argtypes = [wintypes.HANDLE, wintypes.LPSTR, wintypes.DWORD]
dxva2.CapabilitiesRequestAndCapabilitiesReply.restype  = wintypes.BOOL

# -------------------- Maps --------------------
# Input source VCP 0x60
INPUT_MAP = {
    "vga1":  0x01,
    "dvi1":  0x03,
    "dvi2":  0x04,
    "dp1":   0x0F,
    "dp2":   0x10,
    "hdmi1": 0x11,
    "hdmi2": 0x12,
}

# Power mode VCP 0xD6
POWER_MAP = {
    "on":       0x01,
    "dpms_off": 0x04,  # recommended "screen off"
    "off":      0x05,  # often "stronger" off (write-only on some monitors)
}

@dataclass
class MonInfo:
    idx: int
    name: str
    handle: int
    caps: str
    model_tag: str
    supp_input: set[int]
    supp_power: set[int]

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

def parse_supported_values(caps: str, vcp_hex: int) -> set[int]:
    if not caps:
        return set()
    vcp = f"{vcp_hex:02X}"
    m = re.search(rf"\b{vcp}\(([^)]*)\)", caps, flags=re.IGNORECASE)
    if not m:
        return set()
    tokens = re.findall(r"[0-9A-Fa-f]{2}", m.group(1))
    return {int(t, 16) for t in tokens}

def parse_model_tag(caps: str) -> str:
    # From your outputs: model(RTK) / MStar (sometimes appears as "model(...)" or "MStar" near type)
    m = re.search(r"model\(([^)]+)\)", caps, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # fallback: try common tokens
    for token in ["MStar", "RTK"]:
        if re.search(rf"\b{token}\b", caps, flags=re.IGNORECASE):
            return token
    return "unknown"

def vcp_get(hmon, code_hex: int):
    vct = wintypes.DWORD(0)
    cur = wintypes.DWORD(0)
    mx  = wintypes.DWORD(0)
    ok = dxva2.GetVCPFeatureAndVCPFeatureReply(
        hmon,
        wintypes.BYTE(code_hex),
        ctypes.byref(vct),
        ctypes.byref(cur),
        ctypes.byref(mx),
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
            supp_60 = parse_supported_values(caps, 0x60)
            supp_d6 = parse_supported_values(caps, 0xD6)
            tag = parse_model_tag(caps)
            infos.append(MonInfo(
                idx=i,
                name=str(pm.szPhysicalMonitorDescription),
                handle=pm.hPhysicalMonitor,
                caps=caps,
                model_tag=tag,
                supp_input=supp_60,
                supp_power=supp_d6,
            ))
        return infos, phys
    except Exception:
        # If something fails mid-way, still destroy handles
        destroy_physical(phys)
        raise

def select_by_model(infos, model_keyword: str) -> MonInfo:
    key = model_keyword.strip().lower()
    hits = [m for m in infos if key in m.model_tag.lower() or key in m.caps.lower() or key in m.name.lower()]
    if not hits:
        raise ValueError(f"No monitor matched keyword '{model_keyword}'. Use `list` to see available tags.")
    if len(hits) > 1:
        # If multiple match, prefer exact model_tag match
        exact = [m for m in hits if m.model_tag.lower() == key]
        if len(exact) == 1:
            return exact[0]
        raise ValueError(f"Keyword '{model_keyword}' matched multiple monitors: {[h.model_tag for h in hits]}")
    return hits[0]

def cmd_list(infos):
    for m in infos:
        print(f"[{m.idx}] {m.name}")
        print(f"  model_tag: {m.model_tag}")
        if m.supp_power:
            print("  power(0xD6):", " ".join(f"0x{x:02X}" for x in sorted(m.supp_power)))
        else:
            print("  power(0xD6): (unknown)")
        if m.supp_input:
            print("  input(0x60):", " ".join(f"0x{x:02X}" for x in sorted(m.supp_input)))
        else:
            print("  input(0x60): (unknown)")
        print()

def cmd_power(target: MonInfo, mode: str):
    val = POWER_MAP[mode]
    if target.supp_power and val not in target.supp_power:
        raise ValueError(f"Monitor[{target.idx}] does not advertise power value 0x{val:02X}")
    vcp_set(target.handle, 0xD6, val)
    time.sleep(0.2)
    got = vcp_get(target.handle, 0xD6)
    print(f"OK: power {mode} -> [{target.idx}] tag={target.model_tag}")
    if got is None:
        print("  verify: readback unavailable (some monitors block read for 0xD6)")
    else:
        cur, mx = got
        print(f"  verify: current=0x{cur:02X} max=0x{mx:02X}")

def cmd_input(target: MonInfo, source: str):
    val = INPUT_MAP[source]
    if target.supp_input and val not in target.supp_input:
        raise ValueError(f"Monitor[{target.idx}] does not advertise input value 0x{val:02X}")
    vcp_set(target.handle, 0x60, val)
    time.sleep(0.5)
    got = vcp_get(target.handle, 0x60)
    print(f"OK: input {source} -> [{target.idx}] tag={target.model_tag}")
    if got is None:
        print("  verify: readback unavailable (some monitors block read for 0x60)")
    else:
        cur, mx = got
        print(f"  verify: current=0x{cur:02X} max=0x{mx:02X}")

def cmd_test(infos):
    """
    Non-destructive test:
    - For each monitor, try reading 0x60 and 0xD6 (if readable)
    - Try setting power dpms_off then on (may blank screen briefly)
    - For input: only set if at least two inputs are advertised (otherwise skip)
    """
    print("=== DDC/CI TEST START ===")
    for m in infos:
        print(f"\n-- Monitor [{m.idx}] name={m.name} tag={m.model_tag}")

        # Read current values
        p = vcp_get(m.handle, 0xD6)
        i = vcp_get(m.handle, 0x60)
        print("  read power(0xD6):", "unavailable" if p is None else f"current=0x{p[0]:02X}, max=0x{p[1]:02X}")
        print("  read input(0x60):", "unavailable" if i is None else f"current=0x{i[0]:02X}, max=0x{i[1]:02X}")

        # Power toggle test (brief blanking)
        if m.supp_power and 0x04 in m.supp_power and 0x01 in m.supp_power:
            print("  power toggle: dpms_off -> on")
            vcp_set(m.handle, 0xD6, 0x04)
            time.sleep(1.0)
            vcp_set(m.handle, 0xD6, 0x01)
            time.sleep(0.5)
            print("  power toggle: done")
        else:
            print("  power toggle: skipped (caps do not show 0x04 and 0x01)")

        # Input test (only if multiple sources advertised)
        if len(m.supp_input) >= 2:
            # Choose two sources deterministically
            vals = sorted(m.supp_input)
            a, b = vals[0], vals[1]
            print(f"  input toggle: 0x{a:02X} -> 0x{b:02X} -> back")
            vcp_set(m.handle, 0x60, a)
            time.sleep(1.0)
            vcp_set(m.handle, 0x60, b)
            time.sleep(1.0)
            vcp_set(m.handle, 0x60, a)
            time.sleep(0.5)
            print("  input toggle: done")
        else:
            print("  input toggle: skipped (not enough inputs advertised)")

    print("\n=== DDC/CI TEST END ===")
    print("If you saw no [ERROR] and the monitors behaved as expected, packaging to EXE is safe.")

def main():
    if sys.platform != "win32":
        print("[ERROR] Windows only.")
        return 1

    ap = argparse.ArgumentParser(description="DDC/CI monitor manager (stable selection by model keyword)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="List monitors + model tags + supported values")

    pwr = sub.add_parser("power", help="Set power mode (VCP 0xD6)")
    pwr.add_argument("--model", required=True, help="keyword to select monitor (e.g. RTK or MStar)")
    pwr.add_argument("mode", choices=list(POWER_MAP.keys()))

    inp = sub.add_parser("input", help="Set input source (VCP 0x60)")
    inp.add_argument("--model", required=True, help="keyword to select monitor (e.g. RTK or MStar)")
    inp.add_argument("source", choices=list(INPUT_MAP.keys()))

    sub.add_parser("test", help="Run quick test (power toggle + optional input toggle)")

    args = ap.parse_args()

    infos, phys = build_mon_infos()
    try:
        if args.cmd == "list":
            cmd_list(infos)
            return 0
        if args.cmd == "test":
            cmd_test(infos)
            return 0
        if args.cmd == "power":
            target = select_by_model(infos, args.model)
            cmd_power(target, args.mode)
            return 0
        if args.cmd == "input":
            target = select_by_model(infos, args.model)
            cmd_input(target, args.source)
            return 0
        return 2
    except Exception as e:
        print(f"[ERROR] {e}")
        return 1
    finally:
        destroy_physical(phys)

if __name__ == "__main__":
    raise SystemExit(main())