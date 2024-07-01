"""Module responsible for performing speedtest and returning output
to the main part of the code"""

import json
import speedtest


def run_test():
    """Performs speedtest
    returns download_speed: float, upload_speed: float, ping: float"""
    st = speedtest.Speedtest()

    st.get_best_server()

    result_download_speed = st.download() / 1_000_000
    result_upload_speed = st.upload() / 1_000_000

    result_ping = st.results.ping

    return (result_download_speed, result_upload_speed, result_ping)


if __name__ == "__main__":
    download_speed, upload_speed, ping = run_test()
    results = {
        "download_speed": f"{round(download_speed, 2)} Mbps",
        "upload_speed": f"{round(upload_speed, 2)} Mbps",
        "ping": f"{round(ping, 2)} ms",
    }

    print(json.dumps(results))
