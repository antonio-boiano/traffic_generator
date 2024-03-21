# Traffic generator

A useful python3 framework that generate traffic of multiples types of tcp protocol.

## Usage

Clone the repo and do

```bash
cd framework
python3 traffic_generator.py traffic_type mode [--ip] [-p | --port]
```

Options:
- traffic_type modes = iperf, http, mqtt, audio, video, torrent, sftp, telegram
- mode = server, client, broker, publisher, subscriber (Check which mode is available for every protocol).

## Credits

- http protocol: https://github.com/1tayH/noisy.git
- MQTT: https://isurunuwanthilaka.medium.com/get-into-mqtt-in-2-minutes-python-docker-5d4e8b55cf1c (communication between containers).
