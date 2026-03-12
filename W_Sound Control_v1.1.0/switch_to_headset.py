from audio_switch_common import switch_profile

PROFILE_NAME = "Headset"
INPUT_DEVICE_ID = "{0.0.1.00000000}.{3ec6b11b-b0eb-4a02-85c3-5b115ed9d18c}"
OUTPUT_DEVICE_ID = "{0.0.0.00000000}.{723130b9-1173-4c90-812e-38deb9bf8d2b}"

if __name__ == "__main__":
    success = switch_profile(PROFILE_NAME, INPUT_DEVICE_ID, OUTPUT_DEVICE_ID)
    if not success:
        print("Headset profile was not applied.")