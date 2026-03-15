import queue
import threading
from typing import Callable

import comtypes
import keyboard
import pystray
from PIL import Image, ImageDraw

from profile_manager import apply_profile, get_available_profiles, load_config, load_profiles

request_queue: "queue.Queue[str | None]" = queue.Queue()


def create_icon_image() -> Image.Image:
    width, height = 64, 64
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    draw.rectangle((14, 24, 26, 40), fill=(52, 120, 246, 255))
    draw.polygon([(26, 24), (40, 16), (40, 48), (26, 40)], fill=(52, 120, 246, 255))
    draw.arc((38, 18, 52, 46), start=300, end=60, fill=(52, 120, 246, 255), width=4)
    draw.arc((42, 12, 60, 52), start=300, end=60, fill=(52, 120, 246, 180), width=4)

    return image


def enqueue_profile(profile_name: str) -> None:
    request_queue.put(profile_name)


def make_profile_action(profile_name: str) -> Callable:
    def action(icon: pystray.Icon, item) -> None:
        enqueue_profile(profile_name)
        try:
            icon.notify(f"Requested: {profile_name}", "W_Sound Control")
        except Exception:
            pass
    return action


def show_available_profiles(icon: pystray.Icon, item) -> None:
    lines = []
    for profile in get_available_profiles():
        status = "OK" if profile["available"] else "NOT AVAILABLE"
        lines.append(f"{profile['name']}: {status}")
    try:
        icon.notify("\n".join(lines), "Audio Profiles")
    except Exception:
        pass


def reload_hotkeys(icon: pystray.Icon, item) -> None:
    keyboard.clear_all_hotkeys()
    register_hotkeys(icon)
    try:
        icon.notify("Hotkeys reloaded", "W_Sound Control")
    except Exception:
        pass


def quit_app(icon: pystray.Icon, item) -> None:
    keyboard.clear_all_hotkeys()
    request_queue.put(None)
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
            enqueue_profile(name)
            try:
                icon.notify(f"Requested: {name}", "W_Sound Control")
            except Exception:
                pass

        keyboard.add_hotkey(hotkey, callback)
        print(f"[HOTKEY] {profile_name} -> {hotkey}")


def hotkey_worker(icon: pystray.Icon) -> None:
    register_hotkeys(icon)
    keyboard.wait()


def audio_worker(icon: pystray.Icon) -> None:
    comtypes.CoInitialize()
    try:
        while True:
            profile_name = request_queue.get()
            if profile_name is None:
                break

            try:
                success = apply_profile(profile_name)
                message = f"{profile_name} applied" if success else f"{profile_name} unavailable"
            except Exception as e:
                message = f"{profile_name} failed: {e}"
                print(f"[ERROR] {message}")

            try:
                icon.notify(message, "W_Sound Control")
            except Exception:
                pass
    finally:
        comtypes.CoUninitialize()


if __name__ == "__main__":
    icon = pystray.Icon(
        "W_Sound_Control",
        create_icon_image(),
        "W_Sound Control v1.2.0",
        build_menu(),
    )

    thread_hotkey = threading.Thread(target=hotkey_worker, args=(icon,), daemon=True)
    thread_hotkey.start()

    thread_audio = threading.Thread(target=audio_worker, args=(icon,), daemon=True)
    thread_audio.start()

    icon.run()