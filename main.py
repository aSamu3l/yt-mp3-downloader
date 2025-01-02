from lockf import LockFolder
import functions as f
from PIL import Image
import customtkinter as CTk
from CTkMessagebox import CTkMessagebox as CTkM
import os
import signal
import threading
import webbrowser
import yt_dlp

baseColor = ("#ebebeb", "#242424")
cardContent = ("#dbdbdb", "#2b2b2b")
boxContent = ("#f9f9fa", "#1d1e1e")

folder = LockFolder()


def on_closing():
    folder.unlock()
    root.destroy()


def handle_exit(signum, frame):
    folder.unlock()
    exit(0)


def destination_folder():
    global folder
    dest = f.select_destination_folder()
    if dest == "":
        return
    destinationFolderPath.set(dest)
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)
    folder.change_path(dest)
    folder.lock()


def tqdm_hook(d):
    if d['status'] == 'downloading':
        downloaded = d['downloaded_bytes']
        total = d['total_bytes']
        progress = downloaded / total
        progress_bar.set(progress)
    elif d['status'] == 'finished':
        progress_bar.set(1.0)
        progress_bar.configure(mode="indeterminate")
        progress_bar.start()


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
        'progress_hooks': [tqdm_hook],
    }

    # Download the audio
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)
            return True
    except Exception as e:
        return False


def get_yt_video_title(url: str) -> str:
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict.get('title', None)


def open_repo(event):
    webbrowser.open_new("https://github.com/aSamu3l/yt-mp3-downloader")


def open_profile(event):
    webbrowser.open_new("https://github.com/aSamu3l/")


def ldya(urll: str, dest: str = "downloads"):
    urlEntry.configure(state="readonly")

    res = download_youtube_audio(urll, dest)
    if res:
        CTkM(title="Success", message="Download completed", icon="info")
    else:
        CTkM(title="Error", message="Download failed", icon="cancel")

    urlEntry.configure(state="normal")
    url.set("")
    progress_bar.configure(mode="determinate")
    progress_bar.set(0.0)
    progress_bar.stop()


def download():
    if not folder.locked:
        CTkM(title="Error", message="Please select a destination folder", icon="cancel")
        return
    if url.get() == "":
        CTkM(title="Error", message="Please enter a URL", icon="cancel")
        return
    threading.Thread(target=ldya, args=(url.get(), destinationFolderPath.get())).start()


CTk.set_appearance_mode("dark")
root = CTk.CTk()
root.geometry("800x450")
root.title("YT MP3 Downloader")
if os.name == "nt":
    root.iconbitmap("./img/icon.ico")
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Download Frame
downloadFrame = CTk.CTkFrame(root, fg_color=cardContent, width=780, height=380)
downloadFrame.pack()
downloadFrame.place(x=10, y=10)

# Download IMG
imgDownload = CTk.CTkImage(Image.open("img/icon.png"), size=(100, 100))

imageFileLabel = CTk.CTkLabel(downloadFrame, image=imgDownload, text="", fg_color=None, width=780)
imageFileLabel.pack()
imageFileLabel.place(x=0, y=10)

# Download Frame Title
downloadFrameTitle = CTk.CTkLabel(downloadFrame, text="YT MP3 DOWNLOADER", bg_color=baseColor, fg_color=cardContent,
                                  width=780, height=30, font=("Arial", 20))
downloadFrameTitle.pack()
downloadFrameTitle.place(x=0, y=100)

# Destination Folder
destinationFolderPath = CTk.StringVar()
destinationFolderPath.set("")
destinationFolderEntry = CTk.CTkEntry(downloadFrame, textvariable=destinationFolderPath, bg_color=boxContent,
                                      fg_color=cardContent, width=760, height=30, font=("Arial", 15), state="readonly")
destinationFolderEntry.pack()
destinationFolderEntry.place(x=10, y=170)
destinationFolderButton = CTk.CTkButton(downloadFrame, text="Select Folder", width=760, height=30, font=("Arial", 15),
                                        command=destination_folder)
destinationFolderButton.pack()
destinationFolderButton.place(x=10, y=210)

# Progress Bar
progress_bar = CTk.CTkProgressBar(downloadFrame, width=760)
progress_bar.pack()
progress_bar.place(x=10, y=362)
progress_bar.set(0)

# URL Label
urlLabel = CTk.CTkLabel(downloadFrame, text="⬇ YouTube URL ⬇", bg_color=baseColor, fg_color=cardContent, width=780, height=30,
                         font=("Arial", 20))
urlLabel.pack()
urlLabel.place(x=0, y=255)

# URL
url = CTk.StringVar()
url.set("")
urlEntry = CTk.CTkEntry(downloadFrame, textvariable=url, bg_color=boxContent, fg_color=cardContent, width=760,
                        height=30, font=("Arial", 15))
urlEntry.pack()
urlEntry.place(x=10, y=285)

# Download Button
downloadButton = CTk.CTkButton(downloadFrame, text="Download", width=760, height=30, font=("Arial", 15),
                               command=download)
downloadButton.pack()
downloadButton.place(x=10, y=325)

# Credit Frame
creditFrame = CTk.CTkFrame(root, fg_color=cardContent, width=780, height=40)
creditFrame.pack()
creditFrame.place(x=10, y=400)

# Credit Frame Content
creditLabel = CTk.CTkLabel(creditFrame, text="Made with ❤ by aSamu3l", font=("Arial", 20), height=20)
creditLabel.pack()
creditLabel.place(x=10, y=10)
creditLabel.bind("<Button-1>", open_profile)

# Credit Frame Image
imgGit = CTk.CTkImage(Image.open("img/git.png"), size=(30, 30))

imageExtLabel = CTk.CTkLabel(creditFrame, image=imgGit, text="", fg_color=None)
imageExtLabel.pack()
imageExtLabel.place(x=745, y=5)
imageExtLabel.bind("<Button-1>", open_repo)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
