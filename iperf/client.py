import os
import argparse

def main(host_ip):
    try:
        # Run iperf in client mode
        # iperf_command = ["iperf", "-c", host]
        os.system(f"iperf3 -c {host_ip}")
        # subprocess.call(iperf_command)
    except Exception as e:
        print(f"Exception: {e}")
        # print("Please specify the host using the --host option in client mode.")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='iperf3 server connection.')

    parser.add_argument('--ip', required=True, help='IP address of the iperf3 server.')

    args = parser.parse_args()
    
    main(args.ip)