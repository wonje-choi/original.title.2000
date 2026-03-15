import threading
from typing import Callable

import keyboard
import pystray
from PIL import Image, ImageDraw

from profile_manager import apply_profile, get_available_profiles, load_config, load_profiles


def create_icon_image() -> Image.Image:
    width, height = 64, 64
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # simple blue speaker icon
    draw.rectangle((14, 24, 26, 40), fill=(52, 120, 246, 255))
    draw.polygon([(26, 24), (40, 16), (40, 48), (26, 40)], fill=(52, 120, 246, 255))
    draw.arc((38, 18, 52, 46), start=300, end=60, fill=(52, 120, 246, 255), width=4)
    draw.arc((42, 12, 60, 52), start=300, end=60, fill=(52, 120, 246, 180), width=4)

    return image


def make_profile_action(profile_name: str) -> Callable:
    def action(icon: pystray.Icon, item) -> None:
        success = apply_profile(profile_name)
        message = f"{profile_name} applied" if success else f"{profile_name} unavailable"
        icon.notify(message, "W_Sound Control")
    return action


def show_available_profiles(icon: pystray.Icon, item) -> None:
    lines = []
    for profile in get_available_profiles():
        status = "OK" if profile["available"] else "NOT AVAILABLE"
        lines.append(f"{profile['name']}: {status}")
    icon.notify("\n".join(lines), "Audio Profiles")


def reload_hotkeys(icon: pystray.Icon, item) -> None:
    keyboard.clear_all_hotkeys()
    register_hotkeys(icon)
    icon.notify("Hotkeys reloaded", "W_Sound Control")


def quit_app(icon: pystray.Icon, item) -> None:
    keyboard.clear_all_hotkeys()
    icon.stop()


def build_menu() -> pystray.Menu:
    profile_items = []
    for profile in load_profiles():
        profile_items.append(
            pystray.MenuItem(
                f"Switch to {profile['name']}",
                make_profile_action(profile["name"]),
            )
        )

    return pystray.Menu(
        *profile_items,
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Show Profile Status", show_available_profiles),
        pystray.MenuItem("Reload Hotkeys", reload_hotkeys),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Exit", quit_app),
    )


def register_hotkeys(icon: pystray.Icon) -> None:
    config = load_config()
    hotkeys = config.get("hotkeys", {})

    for profile_name, hotkey in hotkeys.items():
        def callback(name=profile_name):
            success = apply_profile(name)
            message = f"{name} applied" if success else f"{name} unavailable"
            try:
                icon.notify(message, "W_Sound Control")
            except Exception:
                pass

        keyboard.add_hotkey(hotkey, callback)
        print(f"[HOTKEY] {profile_name} -> {hotkey}")


def hotkey_worker(icon: pystray.Icon) -> None:
    register_hotkeys(icon)
    keyboard.wait()


if __name__ == "__main__":
    icon = pystray.Icon(
        "W_Sound_Control",
        create_icon_image(),
        "W_Sound Control v1.2.0",
        build_menu(),
    )

    thread = threading.Thread(target=hotkey_worker, args=(icon,), daemon=True)
    thread.start()

    icon.run()