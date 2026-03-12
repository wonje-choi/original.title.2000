import json
from pathlib import Path

from audio_switch_common import switch_profile

STATE_FILE = Path("audio_cycle_state.json")

PROFILES = [
    {
        "name": "Speaker",
        "input_id": "{0.0.1.00000000}.{81c3c34c-05af-4a1a-bfa6-6305f52be0a6}",
        "output_id": "{0.0.0.00000000}.{0dde9ae9-88c3-4f64-98b1-cd57d53f8fe2}",
    },
    {
        "name": "Earphone",
        "input_id": "{0.0.1.00000000}.{81c3c34c-05af-4a1a-bfa6-6305f52be0a6}",
        "output_id": "{0.0.0.00000000}.{51cca44f-9e00-44e9-ac99-558462b066b5}",
    },
    {
        "name": "Headset",
        "input_id": "{0.0.1.00000000}.{3ec6b11b-b0eb-4a02-85c3-5b115ed9d18c}",
        "output_id": "{0.0.0.00000000}.{723130b9-1173-4c90-812e-38deb9bf8d2b}",
    },
]


def load_last_index() -> int:
    if not STATE_FILE.exists():
        return -1

    try:
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        index = int(data.get("last_index", -1))
        if -1 <= index < len(PROFILES):
            return index
    except (ValueError, TypeError, json.JSONDecodeError):
        pass

    return -1


def save_last_index(index: int) -> None:
    data = {"last_index": index}
    STATE_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def get_next_index(last_index: int) -> int:
    return (last_index + 1) % len(PROFILES)


if __name__ == "__main__":
    last_index = load_last_index()
    next_index = get_next_index(last_index)
    profile = PROFILES[next_index]

    switch_profile(
        profile["name"],
        profile["input_id"],
        profile["output_id"],
    )

    save_last_index(next_index)
    print(f"Next cycle saved: {profile['name']}")