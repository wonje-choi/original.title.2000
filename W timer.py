
import time

def timer(minutes=30):
    total_seconds = minutes * 60
    print(f"⏱ {minutes}분 타이머 시작!")

    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"\r남은 시간: {mins:02d}:{secs:02d}", end="", flush=True)
        time.sleep(1)

    print("\n\n🔔 타이머 종료!")

timer(30)

