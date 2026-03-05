
import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL("user32", use_last_error=True)
dxva2 = ctypes.WinDLL("dxva2", use_last_error=True)

# --- Win32 / DXVA2 structs ---
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

# --- function prototypes ---
user32.EnumDisplayMonitors.argtypes = [wintypes.HDC, ctypes.c_void_p, MONITORENUMPROC, wintypes.LPARAM]
user32.EnumDisplayMonitors.restype  = wintypes.BOOL

dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR.argtypes = [wintypes.HMONITOR, ctypes.POINTER(wintypes.DWORD)]
dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR.restype  = wintypes.BOOL

dxva2.GetPhysicalMonitorsFromHMONITOR.argtypes = [wintypes.HMONITOR, wintypes.DWORD, ctypes.POINTER(PHYSICAL_MONITOR)]
dxva2.GetPhysicalMonitorsFromHMONITOR.restype  = wintypes.BOOL

dxva2.DestroyPhysicalMonitors.argtypes = [wintypes.DWORD, ctypes.POINTER(PHYSICAL_MONITOR)]
dxva2.DestroyPhysicalMonitors.restype  = wintypes.BOOL

dxva2.GetCapabilitiesStringLength.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
dxva2.GetCapabilitiesStringLength.restype  = wintypes.BOOL

dxva2.CapabilitiesRequestAndCapabilitiesReply.argtypes = [wintypes.HANDLE, wintypes.LPSTR, wintypes.DWORD]
dxva2.CapabilitiesRequestAndCapabilitiesReply.restype  = wintypes.BOOL


def winerr(prefix: str):
    err = ctypes.get_last_error()
    raise OSError(err, f"{prefix} (WinError={err})")

def get_caps(hmon: wintypes.HANDLE) -> str:
    length = wintypes.DWORD(0)
    if not dxva2.GetCapabilitiesStringLength(hmon, ctypes.byref(length)):
        # Some monitors block/deny this; that's ok.
        return ""
    buf = (ctypes.c_char * (length.value + 1))()
    if not dxva2.CapabilitiesRequestAndCapabilitiesReply(hmon, buf, length):
        return ""
    try:
        return bytes(buf).split(b"\x00", 1)[0].decode("ascii", errors="replace")
    except Exception:
        return ""

def main():
    physical = []

    @MONITORENUMPROC
    def cb(hMonitor, hdc, lprect, lparam):
        count = wintypes.DWORD(0)
        if not dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR(hMonitor, ctypes.byref(count)):
            return True

        arr = (PHYSICAL_MONITOR * count.value)()
        if not dxva2.GetPhysicalMonitorsFromHMONITOR(hMonitor, count, arr):
            return True

        for i in range(count.value):
            physical.append(arr[i])

        # Do NOT destroy here; we still want to use handles later in this run
        return True

    if not user32.EnumDisplayMonitors(None, None, cb, 0):
        winerr("EnumDisplayMonitors failed")

    print("DDC/CI physical monitors found:")
    for idx, pm in enumerate(physical):
        name = pm.szPhysicalMonitorDescription
        caps = get_caps(pm.hPhysicalMonitor)
        print(f"\n[{idx}] {name}")
        if caps:
            # Print a short excerpt so output isn't huge
            excerpt = caps if len(caps) <= 300 else (caps[:300] + " ...")
            print(f"  capabilities: {excerpt}")
        else:
            print("  capabilities: (unavailable)")

    # Clean up handles
    if physical:
        arr = (PHYSICAL_MONITOR * len(physical))(*physical)
        dxva2.DestroyPhysicalMonitors(len(physical), arr)

if __name__ == "__main__":
    main()

