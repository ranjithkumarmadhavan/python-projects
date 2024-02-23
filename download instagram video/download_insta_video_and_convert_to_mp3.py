import instaloader
import os
from moviepy.editor import *

ig = instaloader.Instaloader()

username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
ig.login(username, password)

post_url = input("enter the instagram post url: ")
post = instaloader.Post.from_shortcode(ig.context, post_url.rsplit('/', 1)[-1])
ig.download_post(post, target="video")

# Get all files in the current directory with .mp4 extension
video_files = [file for file in os.listdir('video') if file.endswith('.mp4')]
if not video_files:
    print("No .mp4 files found in the current directory.")
else:
    for video_filename in video_files:
        video_filename = "video/" + video_filename
        # Convert video to audio (MP3)
        video = VideoFileClip(video_filename)
        audio = video.audio

        # Save audio as MP3
        audio_filename = video_filename.replace(".mp4", ".mp3")
        audio.write_audiofile(audio_filename)

        # Close the video and audio files
        video.close()
        audio.close()

        print("Audio extracted and saved as:", audio_filename)