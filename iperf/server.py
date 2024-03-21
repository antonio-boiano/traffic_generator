import os
import argparse

def main(port):
    try:
        # Run iperf in server mode
        # iperf_command = ["iperf", "-s", "-p", str(port)]
        os.system(f"iperf3 -s -p {str(port)}")
        # subprocess.call(iperf_command)
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate Mosquitto configuration file')

    parser.add_argument('--port', default=5201, help='IP address for the Mosquitto listener')

    args = parser.parse_args()

    main(args.port)