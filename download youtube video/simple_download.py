from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=Jc74bcXLxqE')

video_stream = yt.streams.get_highest_resolution()
# Download the video
print(f"Downloading: {yt.title}")
video_stream.download(".")
print("Download complete!")
