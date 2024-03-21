import paho.mqtt.client as mqtt
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
        print("Subscriber connected with result code "+str(rc))
        # Subscribe to the topic
        client.subscribe(TOPIC)

    # Callback function on receiving a message
    def on_message(client, userdata, msg):
        print(f"Received message: {msg.payload.decode()}")

    # Create an MQTT client instance
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the broker
    client.connect(BROKER_ADDRESS, PORT, 60)

    # Loop to process received messages
    client.loop_forever()


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Generate Mosquitto configuration file')
    parser.add_argument('--port', type=int, default=1883, help='Port for the Mosquitto listener')
    parser.add_argument('--ip', required=True, help='IP address for the Mosquitto listener')
    parser.add_argument('--config-file', default='./mosquitto.conf', help='Path to the Mosquitto configuration file')

    args = parser.parse_args()
    
    main()