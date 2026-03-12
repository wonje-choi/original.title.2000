from audio_switch_common import switch_profile, get_profile_availability

PROFILES = {
    "1": {
        "name": "Speaker",
        "input_id": "{0.0.1.00000000}.{81c3c34c-05af-4a1a-bfa6-6305f52be0a6}",
        "output_id": "{0.0.0.00000000}.{0dde9ae9-88c3-4f64-98b1-cd57d53f8fe2}",
    },
    "2": {
        "name": "Earphone",
        "input_id": "{0.0.1.00000000}.{81c3c34c-05af-4a1a-bfa6-6305f52be0a6}",
        "output_id": "{0.0.0.00000000}.{51cca44f-9e00-44e9-ac99-558462b066b5}",
    },
    "3": {
        "name": "Headset",
        "input_id": "{0.0.1.00000000}.{3ec6b11b-b0eb-4a02-85c3-5b115ed9d18c}",
        "output_id": "{0.0.0.00000000}.{723130b9-1173-4c90-812e-38deb9bf8d2b}",
    },
}


def print_menu() -> None:
    print("=" * 32)
    print("Audio Device Selector")
    print("=" * 32)
    print("1. Speaker")
    print("2. Earphone")
    print("3. Headset")
    print("q. Quit")
    print("-" * 32)


if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Select device: ").strip().lower()

        if choice == "q":
            print("Exit.")
            break

        profile = PROFILES.get(choice)
        if profile is None:
            print("Invalid selection. Try again.\n")
            continue

        available, reason = get_profile_availability(
            profile["input_id"],
            profile["output_id"],
        )

        if not available:
            print(f"[NOT AVAILABLE] {profile['name']}")
            print(reason)
            print()
            continue

        switch_profile(
            profile["name"],
            profile["input_id"],
            profile["output_id"],
        )
        break