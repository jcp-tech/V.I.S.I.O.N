# YouTube Video Downloader

A simple command-line tool to download YouTube videos as MP4 files.

## Installation

### 1. Install Python dependencies

```bash
pip install yt-dlp
```

Or install all project dependencies:

```bash
pip install -r ../requirements.txt
```

### 2. Install ffmpeg (Optional but Recommended)

**ffmpeg** is required for downloading the best quality videos. Without it, you'll still be able to download videos, but they may be in lower quality.

#### Windows:
1. Download ffmpeg from: https://ffmpeg.org/download.html
2. Or use Chocolatey: `choco install ffmpeg`
3. Or use Scoop: `scoop install ffmpeg`

#### Mac:
```bash
brew install ffmpeg
```

#### Linux:
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch
sudo pacman -S ffmpeg
```

After installation, restart your terminal and verify with:
```bash
ffmpeg -version
```

## Usage

Run the downloader from the command line:

```bash
python downloader.py <youtube_url>
```

### Example

```bash
python downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

The video will be downloaded to the `downloads/` folder with the video's title as the filename.

## Features

- Downloads videos in the best available MP4 quality
- Shows download progress (percentage, speed, ETA)
- Automatically creates the downloads folder if it doesn't exist
- Handles video and audio merging automatically
- User-friendly error messages

## Troubleshooting

If you encounter any issues:
- Make sure you have a stable internet connection
- Verify the YouTube URL is correct and the video is accessible
- Check that you have write permissions in the downloads folder
