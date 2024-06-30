import speedtest
import json


def run_test():
    st = speedtest.Speedtest()

    st.get_best_server()

    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000

    ping = st.results.ping

    return (download_speed, upload_speed, ping)


if __name__ == "__main__":
    download_speed, upload_speed, ping = run_test()
    results = {
        "download_speed": f"{round(download_speed, 2)} Mbps",
        "upload_speed": f"{round(upload_speed, 2)} Mbps",
        "ping": f"{round(ping, 2)} ms",
    }

    print(json.dumps(results))
