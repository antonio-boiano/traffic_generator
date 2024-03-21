import pandas as pd
from matplotlib.widgets import CheckButtons
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Read the CSV file into a pandas DataFrame
df_mqtt = pd.read_csv('/Users/alexboving/Desktop/Copie des données/Data-Analysis/flower-1-mqtt.csv')
df_https = pd.read_csv('/Users/alexboving/Desktop/Copie des données/Data-Analysis/flower-4-https.csv')
df_sftp = pd.read_csv('/Users/alexboving/Desktop/Copie des données/Data-Analysis/flower-3-sftp.csv')
df_video = pd.read_csv('/Users/alexboving/Desktop/Copie des données/Data-Analysis/flower-8-video.csv')
df_audio = pd.read_csv('/Users/alexboving/Desktop/Copie des données/Data-Analysis/flower-7-audio.csv')
df_torrent = pd.read_csv('/Users/alexboving/Desktop/Copie des données/Data-Analysis/flower-torrent.csv')

# Filter the DataFrame to include only 'flower client' data
# Sampled from mqtt but for a sample to be taken, 
# the properties of the samples must be the same
# compared to all of the other samples.
flower_data = df_mqtt[df_mqtt['Protocol'] == 'TCP']

# Filter the DataFrame to include only 'mqtt protocol' data
mqtt_data = df_mqtt[df_mqtt['Protocol'] == 'MQTT']

# Filter the DataFrame to include only 'https protocol' data
https_data = df_https[df_https['Protocol'] == 'TLSv1.3']

# Filter the DataFrame to include only 'sftp protocol' data
sftp_data = df_sftp[df_sftp['Protocol'] == 'SSHv2']

# Filter the DataFrame to include only 'audio protocol' data
audio_data = df_audio[df_audio['Protocol'] == 'TLSv1.3'].iloc[::5]

# Filter the DataFrame to include only 'torrent protocol' data
torrent_data = df_torrent[df_torrent['Protocol'] == 'UDP']

# Filter the DataFrame to include only 'video protocol' data
video_data = df_video[df_video['Protocol'] == 'TLSv1.3'].iloc[::10]

# ... existing code ...

# Convert video_data DataFrame to CSV
video_data.to_csv('/Users/alexboving/Desktop/Copie des données/Data-Analysis/video_data.csv', index=False)

# ... remaining code ...


# Plot the data with a dotted line
fig, ax = plt.subplots()
mqtt_line, = ax.plot(mqtt_data['Time'], mqtt_data['Length'], linestyle='-.', label='MQTT')
flower_line, = ax.plot(flower_data['Time'], flower_data['Length'], linestyle='solid', label='Flower client')
https_line, = ax.plot(https_data['Time'], https_data['Length'], linestyle='-.', label='HTTPS')
sftp_line, = ax.plot(sftp_data['Time'], sftp_data['Length'], linestyle='-.', label='SFTP')
video_line, = ax.plot(video_data['Time'], video_data['Length'], linestyle='-.', label='Video (1 sample per 10)')
torrent_line, = ax.plot(torrent_data['Time'], torrent_data['Length'], linestyle='-.', label='Torrent')
audio_line, = ax.plot(audio_data['Time'], audio_data['Length'], linestyle='-.', label='Audio (1 sample per 5)')
lines = [mqtt_line, flower_line, https_line, sftp_line, video_line, torrent_line, audio_line]
fig.subplots_adjust(left=0.3)
plt.xlabel('Time [s]')
plt.ylabel('Bytes [B]')
plt.title('Audio Streaming Packet Length over Time')

# Add legend
plt.legend(loc='upper right')

rax = fig.add_axes([0.025, 0.4, 0.2, 0.2])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)

def handleClick(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()

check.on_clicked(handleClick)

plt.show()

plt.legend()
 
rax = fig.add_axes([0.025, 0.4, 0.2, 0.2])
labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visibility)
 
 
def handleClick(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()
 
check.on_clicked(handleClick)

plt.show()