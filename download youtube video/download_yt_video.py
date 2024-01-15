import yt_dlp
import requests

def download_video(video_url, output_path="."):
    opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s"
    }

    ydl = yt_dlp.YoutubeDL(opts)

    ydl.download([video_url])

    video_info = ydl.extract_info(video_url, download=False)

    thumbnail_url = video_info["thumbnail"]
    clean_title = video_info['title'].replace("#","_").replace("|","_")
    thumbnail_path = f"{output_path}/{clean_title}_thumbnail.jpg"

    thumbnail_file = open(thumbnail_path, "wb")
    thumbnail_file.write(requests.get(thumbnail_url).content)
    thumbnail_file.close()

    tags = video_info.get("tags",[])
    print(f"Video Tags: ", tags)

if __name__ == "__main__":
    video_url = input("Enter the Youtube video URL: ")

    output_path = input("Enter the output path (press enter for current directory): ")

    if not output_path:
        output_path = "."

    download_video(video_url, output_path)