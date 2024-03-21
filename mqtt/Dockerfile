FROM ubuntu:22.04

RUN apt-get update && apt-get install -y iputils-ping python3-pip software-properties-common net-tools
RUN pip3 install paho-mqtt
RUN add-apt-repository ppa:mosquitto-dev/mosquitto-ppa
RUN apt-get -y install mosquitto mosquitto-clients

WORKDIR /app

COPY publisher.py /app/publisher.py
COPY subscriber.py /app/subscriber.py
COPY mqtt.py /app/mqtt.py

EXPOSE 1883
