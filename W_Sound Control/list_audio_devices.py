
import json
import warnings

from pycaw.constants import DEVICE_STATE, EDataFlow, ERole
from pycaw.pycaw import AudioUtilities


def get_active_devices(flow):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        return AudioUtilities.GetAllDevices(
            data_flow=flow.value,
            device_state=DEVICE_STATE.ACTIVE.value,
        )


def get_default_device(flow):
    enumerator = AudioUtilities.GetDeviceEnumerator()
    endpoint = enumerator.GetDefaultAudioEndpoint(
        flow.value,
        ERole.eMultimedia.value,
    )
    return AudioUtilities.CreateDevice(endpoint)


def safe_name(device):
    return device.FriendlyName or "(no friendly name)"


def build_report():
    default_output = get_default_device(EDataFlow.eRender)
    default_input = get_default_device(EDataFlow.eCapture)

    report = {
        "output_devices": [],
        "input_devices": [],
    }

    for dev in get_active_devices(EDataFlow.eRender):
        report["output_devices"].append(
            {
                "default_multimedia": dev.id == default_output.id,
                "name": safe_name(dev),
                "id": dev.id,
            }
        )

    for dev in get_active_devices(EDataFlow.eCapture):
        report["input_devices"].append(
            {
                "default_multimedia": dev.id == default_input.id,
                "name": safe_name(dev),
                "id": dev.id,
            }
        )

    return report


if __name__ == "__main__":
    data = build_report()

    print("=== OUTPUT DEVICES (eRender) ===")
    for i, dev in enumerate(data["output_devices"], 1):
        mark = "*" if dev["default_multimedia"] else " "
        print(f"{mark} [{i}] {dev['name']}")
        print(f"    id: {dev['id']}")

    print("\n=== INPUT DEVICES (eCapture) ===")
    for i, dev in enumerate(data["input_devices"], 1):
        mark = "*" if dev["default_multimedia"] else " "
        print(f"{mark} [{i}] {dev['name']}")
        print(f"    id: {dev['id']}")

    with open("audio_devices.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\nSaved: audio_devices.json")
    print("* 표시 = 현재 Multimedia 기본 장치")