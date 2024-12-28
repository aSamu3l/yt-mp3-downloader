from download import download_youtube_audio as dya
from lockf import LockFolder
import functions as f
from PIL import Image
import customtkinter as CTk
from CTkMessagebox import CTkMessagebox as CTkM
import os
import signal
import threading
import webbrowser

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


def open_repo(event):
    webbrowser.open_new("https://github.com/aSamu3l/yt-mp3-downloader")


def open_profile(event):
    webbrowser.open_new("https://github.com/aSamu3l/")


def ldya(urll: str, dest: str = "downloads"):
    urlEntry.configure(state="readonly")
    res = dya(urll, dest)
    if res:
        CTkM(title="Success", message="Download completed", icon="info")
    else:
        CTkM(title="Error", message="Download failed", icon="cancel")
    urlEntry.configure(state="normal")
    url.set("")


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
root.title("File Order")
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
destinationFolderEntry.place(x=10, y=180)
destinationFolderButton = CTk.CTkButton(downloadFrame, text="Select Folder", width=760, height=30, font=("Arial", 15),
                                        command=destination_folder)
destinationFolderButton.pack()
destinationFolderButton.place(x=10, y=220)

# URL Label
urlLabel = CTk.CTkLabel(downloadFrame, text="⬇ YouTube URL ⬇", bg_color=baseColor, fg_color=cardContent, width=780, height=30,
                         font=("Arial", 20))
urlLabel.pack()
urlLabel.place(x=0, y=270)

# URL
url = CTk.StringVar()
url.set("")
urlEntry = CTk.CTkEntry(downloadFrame, textvariable=url, bg_color=boxContent, fg_color=cardContent, width=760,
                        height=30, font=("Arial", 15))
urlEntry.pack()
urlEntry.place(x=10, y=300)

# Download Button
downloadButton = CTk.CTkButton(downloadFrame, text="Download", width=760, height=30, font=("Arial", 15),
                               command=download)
downloadButton.pack()
downloadButton.place(x=10, y=340)

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
