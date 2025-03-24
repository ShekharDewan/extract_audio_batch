import subprocess
import json
import os

VIDEO_EXTENSIONS = ['.mp4', '.mov', '.mkv', '.avi', '.flv', '.webm', '.wmv', '.m4v']

def get_audio_codec(video_path):
    """Detect audio codec using ffprobe."""
    cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=codec_name",
        "-of", "json",
        video_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe error: {result.stderr}")
    
    info = json.loads(result.stdout)
    return info['streams'][0]['codec_name']

def get_audio_extension(codec_name):
    """Map codec to standard audio file extension."""
    mapping = {
        'aac': 'm4a',
        'mp3': 'mp3',
        'opus': 'opus',
        'vorbis': 'ogg',
        'flac': 'flac',
        'ac3': 'ac3',
        'pcm_s16le': 'wav',
        'alac': 'm4a'
    }
    return mapping.get(codec_name, codec_name)

def extract_audio(video_path, output_dir):
    """Extract audio from a video file into specified output folder."""
    try:
        codec = get_audio_codec(video_path)
        ext = get_audio_extension(codec)

        filename = os.path.splitext(os.path.basename(video_path))[0]
        output_path = os.path.join(output_dir, f"{filename}_audio.{ext}")

        if os.path.exists(output_path):
            print(f"Skipping (already exists): {output_path}")
            return

        cmd = [
            "ffmpeg",
            "-i", video_path,
            "-vn",
            "-acodec", "copy",
            output_path
        ]
        print(f"Extracting audio from {filename} → {os.path.basename(output_path)}")
        subprocess.run(cmd, check=True)
        print("✔ Done.")
    except Exception as e:
        print(f"❌ Failed to extract from {video_path}: {e}")

def process_folder(input_dir, output_dir):
    """Process all video files from input_dir and save to output_dir."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        if os.path.isfile(filepath) and os.path.splitext(filename)[1].lower() in VIDEO_EXTENSIONS:
            extract_audio(filepath, output_dir)

# === Entry Point ===
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(base_dir, "input_videos")
    output_folder = os.path.join(base_dir, "output_audio")

    process_folder(input_folder, output_folder)
