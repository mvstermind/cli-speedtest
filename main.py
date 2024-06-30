import speedtest


def run_test():
    st = speedtest.Speedtest()

    st.get_best_server()

    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000

    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")


if __name__ == "__main__":
    run_test()
