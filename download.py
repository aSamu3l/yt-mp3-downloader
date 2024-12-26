import yt_dlp
import os


def download_youtube_audio(url: str, output_path: str = "downloads") -> bool:
    # Ensure the output path exists
    os.makedirs(output_path, exist_ok=True)

    # Define options for yt-dlp to download audio and select the output path
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Specify output path
    }

    # Download the audio
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)
            return True
    except Exception as e:
        return False


def main():
    youtube_url = input("Enter the YouTube URL: ")
    download_path = "downloads"  # Folder to save the files (OPTIONAL)

    download_youtube_audio(youtube_url, download_path)


if __name__ == "__main__":
    main()

# Code from my contribution to this project: https://github.com/markuZZalo/YouTube-to-.mp3-converter