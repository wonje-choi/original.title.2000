import sys

from profile_manager import apply_profile, get_available_profiles


def print_usage() -> None:
    print("Usage:")
    print("  py switch_by_profile.py Speaker")
    print("  py switch_by_profile.py Earphone")
    print("  py switch_by_profile.py Headset")
    print()
    print("Available profiles:")
    for profile in get_available_profiles():
        status = "OK" if profile["available"] else "NOT AVAILABLE"
        print(f"  - {profile['name']} [{status}]")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        raise SystemExit(1)

    profile_name = " ".join(sys.argv[1:])
    success = apply_profile(profile_name)
    raise SystemExit(0 if success else 1)