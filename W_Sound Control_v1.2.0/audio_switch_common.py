import warnings
from typing import Dict, Tuple

from pycaw.constants import DEVICE_STATE, ERole
from pycaw.pycaw import AudioUtilities

ALL_ROLES = [ERole.eConsole, ERole.eMultimedia, ERole.eCommunications]


def get_active_device_map() -> Dict[str, object]:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        devices = AudioUtilities.GetAllDevices(
            device_state=DEVICE_STATE.ACTIVE.value,
        )
    return {device.id: device for device in devices}


def get_profile_availability(input_device_id: str, output_device_id: str) -> Tuple[bool, str]:
    device_map = get_active_device_map()

    missing = []
    if input_device_id not in device_map:
        missing.append(f"Input device missing: {input_device_id}")
    if output_device_id not in device_map:
        missing.append(f"Output device missing: {output_device_id}")

    if missing:
        return False, "\n".join(missing)

    return True, "OK"


def set_default_device(device_id: str) -> None:
    if not hasattr(AudioUtilities, "SetDefaultDevice"):
        raise RuntimeError(
            "This pycaw version does not support SetDefaultDevice(). "
            "Please upgrade pycaw."
        )
    AudioUtilities.SetDefaultDevice(device_id, ALL_ROLES)


def switch_profile(profile_name: str, input_device_id: str, output_device_id: str) -> bool:
    device_map = get_active_device_map()

    if input_device_id not in device_map:
        print(f"[SKIP] {profile_name}")
        print("Reason: input device is not connected or not active.")
        print(f"Input ID: {input_device_id}")
        return False

    if output_device_id not in device_map:
        print(f"[SKIP] {profile_name}")
        print("Reason: output device is not connected or not active.")
        print(f"Output ID: {output_device_id}")
        return False

    input_device = device_map[input_device_id]
    output_device = device_map[output_device_id]

    set_default_device(output_device_id)
    set_default_device(input_device_id)

    print(f"[OK] {profile_name}")
    print(f"Input : {input_device.FriendlyName}")
    print(f"Output: {output_device.FriendlyName}")
    return True