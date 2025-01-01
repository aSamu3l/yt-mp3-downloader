<p align="center">
  <img src="https://github.com/aSamu3l/yt-mp3-downloader/blob/main/img/logo.png?raw=true" alt="Logo">
</p>

# YouTube MP3 DOWNLOADER

This project was born from the need to download some music on the fly to always have it available offline. So I thought of writing this code that creates a fast and intuitive graphical interface to download some songs on the fly.

## Installation

### Requirements
- Python 3.6 or higher
- pip
- ffmpeg

### Installation
1. Clone the repository
```bash
git clone https://github.com/aSamu3l/yt-mp3-downloader.git
cd yt-mp3-downloader
```

2. Install the required packages
```bash
pip install -r requirements.txt
```

3. Run the program
```bash
python main.py
```

## Usage
After starting the program, you will see a window like this:
<p align="center">
  <img src="https://github.com/aSamu3l/yt-mp3-downloader/blob/main/extra/screen.png?raw=true" alt="Screen">
</p>

1. Select the destination folder where the songs will be downloaded
2. Enter the URL of the YouTube video you want to download
3. Click on the "Download" button
4. Wait for the download to finish
5. Enjoy your music!
6. If you want to download another song, insert the new URL and click on the "Download" button again

## Compiling EXE
If you want to compile the program into an executable file, you can use the `auto-py-to-exe` package.

1. Install the package
```bash
pip install auto-py-to-exe
```

2. Run the package
```bash
auto-py-to-exe
```

3. At the end of the page you can import the `exe.json` file. You need to import and change the static files path to the correct path. Then click on the "Convert .py to .exe" button.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Contributing
If you want to contribute to the project, please fork the repository and submit a pull request. I will be happy to review and accept it.