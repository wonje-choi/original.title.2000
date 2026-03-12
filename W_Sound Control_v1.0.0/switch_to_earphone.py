from audio_switch_common import switch_profile

PROFILE_NAME = "Earphone"
INPUT_DEVICE_ID = "{0.0.1.00000000}.{81c3c34c-05af-4a1a-bfa6-6305f52be0a6}"
OUTPUT_DEVICE_ID = "{0.0.0.00000000}.{51cca44f-9e00-44e9-ac99-558462b066b5}"

if __name__ == "__main__":
    switch_profile(PROFILE_NAME, INPUT_DEVICE_ID, OUTPUT_DEVICE_ID)