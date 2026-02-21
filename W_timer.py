import time


def timer(minutes=30, extra_seconds=30):
    total_seconds = minutes * 60
    print(f"{minutes}-minute timer started! (Ctrl+C to stop)")

    try:
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            print(f"\rTime left: {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)

        print("\n\nTimer finished!")

        for elapsed in range(1, extra_seconds + 1):
            mins, secs = divmod(elapsed, 60)
            print(f"\rOvertime: +{mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)

        print("\nDone.")

    except KeyboardInterrupt:
        print("\n\nTimer interrupted.")


if __name__ == "__main__":
    timer(0, 5)
