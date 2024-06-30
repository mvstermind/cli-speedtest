from speed import run_test


def main():
    download_speed, upload_speed, ping = run_test()

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")


if __name__ == "__main__":
    main()
