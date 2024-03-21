FROM anboiano/flbanch_flower:grpc

# Install tcpdump and other necessary tools
RUN apt-get update && apt-get install -y tcpdump iputils-ping xterm python3 python3-pip
RUN apt-get install -y \
    software-properties-common \
    net-tools \
    iputils-ping \
    iproute2

RUN echo "wireshark-common wireshark-common/install-setuid boolean true" | debconf-set-selections
RUN   apt-get install -y tshark

# Install dependencies for protocols
RUN apt install -y iperf3

# Tnstall dependencies for cv2
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6

# Install mplayer for audio streaming
RUN apt-get install -y alsa-base \
        alsa-utils \
        libsndfile1-dev

RUN apt-get install -y mplayer

# Install Mosquitto broker
RUN add-apt-repository ppa:mosquitto-dev/mosquitto-ppa
RUN apt-get -y install mosquitto mosquitto-clients
    
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy your Python script into the container
COPY traffic_generator /app/traffic_generator
COPY traffic_generator/audio/config /app/../root/.mplayer/

# Install any required dependencies (if needed)
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# RUN mkdir /app/saved_output

# Expose the needed port
EXPOSE 22 443 1883 5201 6881 6882 6883 6884 6885 6886 6887 6888 6889 6890 6891 8080 9091 9092 9093
