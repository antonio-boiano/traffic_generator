# torrent_receiver.py
import libtorrent as lt
import os
import time
import argparse

def download_torrent(torrent_path, output_path, ip, port):
    ses = lt.session({'listen_interfaces': f'{ip}:{port}'})
    ses.listen_on(6881, 6891)
    e = lt.bdecode(open(torrent_path, 'rb').read())
    info = lt.torrent_info(e)
    h = ses.add_torrent(info, output_path)
    while not h.is_seed():
        s = h.status()
        print('%.2f%% complete (down: %.1f kB/s, up: %.1f kB/s, peers: %d) %s' % (
            s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
            s.num_peers, s.state))
        
        time.sleep(2)

    print('download complete')


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Generate torrent traffic")

    # Add additional arguments specific to each traffic type (you can expand this as needed)
    parser.add_argument(
        "--ip",
        help="Specify the destination IP address for the traffic generation.",
        required=True, 
        metavar="ip"
    )
    parser.add_argument(
        "-p", 
        "--port",
        type=int,
        default=6881, 
        help="Specify the destination port for the traffic generation.",
        metavar="port"
    )


    # Parse the command line arguments
    args = parser.parse_args()


    torrent_file = "/app/traffic_generator/torrent/test.torrent"
    os.system("rm -r /app/traffic_generator/torrent/test.mp4")

    while True:
        # Get the current working directory
        current_directory = os.getcwd()
        # Create the full path to the file
        torrent_path = os.path.join(current_directory, torrent_file)
        download_torrent(torrent_path, "/app/traffic_generator/torrent/depo/", args.ip, args.port)
        if os.path.isfile("/app/traffic_generator/torrent/depo/test.mp4"):
            print("File downloaded")
            os.system("rm -r /app/traffic_generator/torrent/depo/test.mp4")

if __name__ == "__main__":
    main()