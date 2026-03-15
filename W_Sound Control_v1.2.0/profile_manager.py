import json
from pathlib import Path
from typing import Any, Dict, List

from audio_switch_common import get_profile_availability, switch_profile

BASE_DIR = Path(__file__).resolve().parent
PROFILES_FILE = BASE_DIR / "profiles.json"
CONFIG_FILE = BASE_DIR / "config.json"


def load_json_file(file_path: Path) -> Dict[str, Any]:
    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {file_path}")
    return json.loads(file_path.read_text(encoding="utf-8"))


def load_profiles() -> List[Dict[str, Any]]:
    data = load_json_file(PROFILES_FILE)
    profiles = data.get("profiles", [])
    if not profiles:
        raise ValueError("profiles.json does not contain any profiles.")
    return profiles


def load_config() -> Dict[str, Any]:
    return load_json_file(CONFIG_FILE)


def get_profile_by_name(profile_name: str) -> Dict[str, Any] | None:
    for profile in load_profiles():
        if profile["name"].lower() == profile_name.lower():
            return profile
    return None


def get_available_profiles() -> List[Dict[str, Any]]:
    result = []
    for profile in load_profiles():
        ok, reason = get_profile_availability(
            profile["input_id"],
            profile["output_id"],
        )
        profile_copy = dict(profile)
        profile_copy["available"] = ok
        profile_copy["reason"] = reason
        result.append(profile_copy)
    return result


def apply_profile(profile_name: str) -> bool:
    profile = get_profile_by_name(profile_name)
    if profile is None:
        print(f"[ERROR] Profile not found: {profile_name}")
        return False

    return switch_profile(
        profile["name"],
        profile["input_id"],
        profile["output_id"],
    )