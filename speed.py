import speedtest


def run_test():
    st = speedtest.Speedtest()

    st.get_best_server()

    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000

    ping = st.results.ping

    return (download_speed, upload_speed, ping)


if __name__ == "__main__":
    run_test()
