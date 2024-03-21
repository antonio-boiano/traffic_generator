import subprocess
import os

VIDEO_URL = 'https://www.youtube.com/watch?v=f1A7SdVTlok'

def download_video(video_url):
    while True:
        # Download the YouTube video using youtube-dl
        subprocess.run(['yt-dlp','-o', './video/downloaded_video.mp4', video_url])
        os.system("rm ./video/downloaded_video.mp4.*")

def play_video():
    # Play the downloaded video using a local media player (e.g., VLC)
    subprocess.run(['/Applications/VLC.app/Contents/MacOs/VLC', 'video.mp4'])

if __name__ == '__main__':
    # Replace 'your_video_url' with the actual URL of the YouTube video
    download_video(VIDEO_URL)