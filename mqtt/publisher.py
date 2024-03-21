import paho.mqtt.client as mqtt
import time
import argparse

def main():
# with open('./mosquitto.conf', 'r') as config_file:
#         first_line = config_file.readline().strip()
#         port, ip = first_line.split()[1:]

    print(f"Port: {args.port}, IP: {args.ip}")

    # Define constants
    BROKER_ADDRESS = args.ip
    PORT = args.port
    TOPIC = "test/topic"

    # Callback function on successful connection
    def on_connect(client, userdata, flags, rc):
        print("Publisher connected with result code "+str(rc))

    # Create an MQTT client instance
    client = mqtt.Client()
    client.on_connect = on_connect

    # Connect to the broker
    client.connect(BROKER_ADDRESS, PORT, 60)

    # Start publishing messages
    while True:
        message = "Hello, MQTT!"
        client.publish(TOPIC, message)
        print(f"Published: {message}")
        time.sleep(3)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Mosquitto configuration file')
    parser.add_argument('--port', type=int, default=1883, help='Port for the Mosquitto listener')
    parser.add_argument('--ip', required=True, help='IP address for the Mosquitto listener')
    parser.add_argument('--config-file', default='./mosquitto.conf', help='Path to the Mosquitto configuration file')

    args = parser.parse_args()

    main()