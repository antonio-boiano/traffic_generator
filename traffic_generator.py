import argparse
import os
import datetime
from utils import generate_csv
import logging


timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Define the available traffic types
traffic_types = ["iperf", "http", "mqtt", "audio", "video", "torrent", "sftp", "telegram"]

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Generate different types of network traffic.")

    # Add an argument to specify the type of traffic
    parser.add_argument(
        "traffic_type",
        choices=traffic_types,
        help="Specify the type of traffic to generate (iperf, http, etc...)",
        metavar = "traffic_type"
    )

    # Specify mode
    parser.add_argument("mode", 
        choices=["server", "client", "broker", "publisher", "subscriber"],
        default = "client", 
        help="Mode of operation", 
        metavar="mode"
    )

    # Add additional arguments specific to each traffic type (you can expand this as needed)
    parser.add_argument(
        "--ip",
        help="Specify the destination IP address for the traffic generation.",
        metavar="ip"
    )
    parser.add_argument(
        "-p", 
        "--port",
        type=int,
        default=443,
        help="Specify the destination port for the traffic generation.",
        metavar="port"
    )

    parser.add_argument("--save_path", 
                        type=str, 
                        default="./output", 
                        help="Path to the folder to save the results file")

    parser.add_argument("-a", "--all",
                        help="Run all the scripts all together.",
                        action='store_true')

    # Parse the command line arguments
    args = parser.parse_args()

    # logging_command = f">> traffic_{args.traffic_type}_{timestamp}"
    # Based on the chosen traffic type, call the appropriate function
    try:
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), args.traffic_type)

        generate_csv(file_path=args.save_path, timestamp=timestamp, traffic_type=args.traffic_type, 
                     mode=args.mode, ip=args.ip, port=args.port)

        if args.traffic_type == "http":
            os.system(f"python3 {file_path}/noisy.py --config {file_path}/config.json")

        if args.traffic_type == "mqtt":
            if args.mode == "broker":
                os.system(f"python3 {file_path}/broker.py --ip {args.ip}")

            elif args.mode == "publisher":
                os.system(f"python3 {file_path}/publisher.py --ip {args.ip}")

            elif args.mode == "subscriber":
                os.system(f"python3 {file_path}/subscriber.py --ip {args.ip}")

        if args.traffic_type == "iperf":
            if args.mode == "server":
                os.system(f"python3 {file_path}/server.py")
            else:
                os.system(f"python3 {file_path}/client.py --ip {args.ip}")
        
        if args.traffic_type == "sftp":
            os.system(f"python3 {file_path}/sftp.py")
        
        if args.traffic_type == "telegram":
            os.system(f"python3 {file_path}/bot.py")

        if args.traffic_type == "torrent":
            if args.mode == "client":
                os.system(f"python3 {file_path}/receiver.py --ip {args.ip} --port {args.port}")

            elif args.mode == "server":
                os.system(f"python3 {file_path}/manager.py")
        
        if args.traffic_type == "video":
            os.system(f"python3 {file_path}/video.py")

        if args.traffic_type == "audio":
            os.system(f"python3 {file_path}/audio.py")
    
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == '__main__':
    main()
