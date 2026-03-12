from audio_switch_common import switch_profile

PROFILE_NAME = "Speaker"
INPUT_DEVICE_ID = "{0.0.1.00000000}.{81c3c34c-05af-4a1a-bfa6-6305f52be0a6}"
OUTPUT_DEVICE_ID = "{0.0.0.00000000}.{0dde9ae9-88c3-4f64-98b1-cd57d53f8fe2}"

if __name__ == "__main__":
    switch_profile(PROFILE_NAME, INPUT_DEVICE_ID, OUTPUT_DEVICE_ID)