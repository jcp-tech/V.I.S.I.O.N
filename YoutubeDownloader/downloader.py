"""
YouTube Video Downloader
Downloads YouTube videos as MP4 files to the downloads folder.
"""

import os
import sys
import yt_dlp


def check_ffmpeg():
    """Check if ffmpeg is available."""
    try:
        import subprocess
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        return result.returncode == 0
    except:
        return False


def download_video(url, output_path="downloads"):
    """
    Download a YouTube video as MP4.
    
    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the downloaded video
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Check for ffmpeg and adjust format accordingly
    has_ffmpeg = check_ffmpeg()
    
    if has_ffmpeg:
        # If ffmpeg is available, download best quality (may require merging)
        format_string = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    else:
        # If no ffmpeg, download pre-merged formats only (may be lower quality)
        print("⚠️  ffmpeg not detected. Downloading pre-merged format (may be lower quality).")
        print("   For best quality, install ffmpeg: https://ffmpeg.org/download.html\n")
        # Use format that's guaranteed to be pre-merged
        format_string = 'best[ext=mp4][vcodec^=avc]/best[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': format_string,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': False,
        'no_warnings': False,
        'progress_hooks': [progress_hook],
        'postprocessor_args': ['-codec', 'copy'] if has_ffmpeg else [],
        'prefer_ffmpeg': has_ffmpeg,
    }
    
    try:
        print(f"Downloading video from: {url}")
        print(f"Output directory: {os.path.abspath(output_path)}\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info
            info = ydl.extract_info(url, download=False)
            video_title = info.get('title', 'Unknown')
            print(f"Video: {video_title}\n")
            
            # Download the video
            ydl.download([url])
            
        print(f"\n✓ Download complete! Video saved to: {os.path.abspath(output_path)}")
        return True
        
    except Exception as e:
        print(f"\n✗ Error downloading video: {str(e)}")
        return False


def progress_hook(d):
    """Hook to display download progress."""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rProgress: {percent} | Speed: {speed} | ETA: {eta}", end='')
    elif d['status'] == 'finished':
        print(f"\n\nProcessing video...")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python downloader.py <youtube_url>")
        print("Example: python downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Get the script's directory and set downloads path relative to it
    script_dir = os.path.dirname(os.path.abspath(__file__))
    downloads_path = os.path.join(script_dir, "downloads")
    
    success = download_video(url, downloads_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
