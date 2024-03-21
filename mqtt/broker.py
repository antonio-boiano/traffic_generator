import argparse
import os
import subprocess

def create_mosquitto_config(port, ip, config_file_path):
    config_content = f"listener {port} {ip}\nallow_anonymous true"

    with open(config_file_path, 'w') as config_file:
        config_file.write(config_content)
        print(f"Configuration file '{config_file_path}' created with listener {port} {ip}")

    return port, ip
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Mosquitto configuration file')
    parser.add_argument('--port', type=int, default=1883, help='Port for the Mosquitto listener')
    parser.add_argument('--ip', required=True, help='IP address for the Mosquitto listener')
    parser.add_argument('--config-file', default='./mosquitto.conf', help='Path to the Mosquitto configuration file')

    args = parser.parse_args()

    port, ip = create_mosquitto_config(args.port, args.ip, args.config_file)
    subprocess.run(["mosquitto", "-c", args.config_file])

