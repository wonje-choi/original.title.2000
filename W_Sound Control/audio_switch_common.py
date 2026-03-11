import warnings

from pycaw.constants import DEVICE_STATE, ERole
from pycaw.pycaw import AudioUtilities

ALL_ROLES = [ERole.eConsole, ERole.eMultimedia, ERole.eCommunications]


def get_active_device_map():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        devices = AudioUtilities.GetAllDevices(
            device_state=DEVICE_STATE.ACTIVE.value,
        )
    return {device.id: device for device in devices}


def require_device(device_map, device_id: str, label: str):
    device = device_map.get(device_id)
    if device is None:
        raise RuntimeError(
            f"{label} device not found or inactive.\n"
            f"device_id: {device_id}\n"
            "Run list_audio_devices.py again and check whether the device is connected."
        )
    return device


def set_default_device(device_id: str):
    if not hasattr(AudioUtilities, "SetDefaultDevice"):
        raise RuntimeError(
            "This pycaw version does not support SetDefaultDevice(). "
            "Upgrade pycaw and try again."
        )
    AudioUtilities.SetDefaultDevice(device_id, ALL_ROLES)


def switch_profile(profile_name: str, input_device_id: str, output_device_id: str):
    device_map = get_active_device_map()
    input_device = require_device(device_map, input_device_id, "Input")
    output_device = require_device(device_map, output_device_id, "Output")

    set_default_device(output_device_id)
    set_default_device(input_device_id)

    print(f"[OK] {profile_name}")
    print(f"Input : {input_device.FriendlyName}")
    print(f"Output: {output_device.FriendlyName}")


if __name__ == "__main__":
    raise SystemExit("Import this module from a profile script.")