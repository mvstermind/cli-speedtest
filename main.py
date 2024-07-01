import time
import sys
import threading

from speed import run_test


def animation_template(stop_event):
    animation_frames = "|/-\\"
    while not stop_event.is_set():
        for i in range(4):
            if stop_event.is_set():
                break
            time.sleep(0.2)
            sys.stdout.write(
                "\r Running test: " + animation_frames[i % len(animation_frames)]
            )
            sys.stdout.flush()
    # Clear the line after the animation stops
    sys.stdout.write("\r")


def main():
    stop_event = threading.Event()
    animation_thread = threading.Thread(target=animation_template, args=(stop_event,))

    animation_thread.start()

    download_speed, upload_speed, ping = run_test()

    stop_event.set()
    animation_thread.join()

    # Time.sleep is just for aesthetic reasons
    print(f"Download speed: {round(download_speed,2)} Mbps")
    time.sleep(0.2)
    print(f"Upload speed: {round(upload_speed, 2)} Mbps")
    time.sleep(0.2)
    print(f"Ping: {round(ping,2)} ms")


if __name__ == "__main__":
    main()