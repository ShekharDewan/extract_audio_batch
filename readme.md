# Video to Audio Extractor (Original Quality)

This tool extracts the **original audio stream** from video files **without re-encoding**, preserving the full audio quality. It leverages `ffmpeg` to copy the audio stream directly, ensuring the output matches the source audio exactly. Designed for batch processing, it supports all major video formats and automatically detects the appropriate audio format for output files. This is ideal for tasks like audio editing, analysis, or playback without the video, while maintaining maximum quality.

## Features

- Preserves original audio quality (no re-encoding)
- Automatically detects and sets the correct audio file extension
- Batch processes all video files in a folder
- Skips files already extracted to avoid overwriting
- Compatible with all major video formats

## Folder Structure

```
video-to-audio-extractor/
├── extract_audio_batch.py         # Main script
├── README.md                      # This file
├── LICENSE                        # License file
├── .gitignore                     # Git ignore file
├── input_videos/                  # Directory for video files
│   └── .gitkeep                   # Keeps the empty folder in Git
└── output_audio/                  # Directory for extracted audio
    └── .gitkeep                   # Keeps the empty folder in Git
```

## How to Use

1. Clone this repository or download the project files.
2. Place your video files into the `input_videos/` folder.
3. Run the script:

```bash
python extract_audio_batch.py
```

The script processes all video files in `input_videos/` and saves the extracted audio to `output_audio/`. Output files retain the original base filename with `_audio` appended and the appropriate extension (e.g., `.m4a` for AAC).

### Example

```
input_videos/my_clip.mp4 → output_audio/my_clip_audio.m4a
```

### Usage Notes

- If `input_videos/` is empty, the script exits without action.
- If an output file already exists in `output_audio/`, the script skips that video to prevent overwriting.
- If a video lacks an audio track, the script skips it and logs a message.

## Supported Video Formats

- `.mp4`
- `.mov`
- `.mkv`
- `.avi`
- `.flv`
- `.webm`
- `.wmv`
- `.m4v`

**Note:** The tool supports any format `ffmpeg` can handle, though the above are the most common.

## Dependencies

The tool requires `ffmpeg` installed on your system. Python dependencies can be installed via Conda (recommended) or pip.

### Option 1: Conda (Recommended)

```bash
# Create a new Conda environment
conda create -n video2audio python=3.10 -c conda-forge ffmpeg

# Activate the environment
conda activate video2audio

# Install the Python dependency
conda install -c conda-forge ffmpeg-python
```

### Option 2: pip

First, install `ffmpeg` system-wide:

- **macOS:** `brew install ffmpeg`
- **Ubuntu/Debian:** `sudo apt install ffmpeg`
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add `ffmpeg` to your PATH.

Then, install the Python package:

```bash
pip install ffmpeg-python
```

**Verification:** Ensure `ffmpeg` is installed by running `ffmpeg --version` in your terminal.

## Notes

- Audio extraction uses `ffmpeg`'s `-acodec copy` option, avoiding re-encoding for optimal quality.
- Output filenames follow the pattern `originalname_audio.extension`, with extensions based on the source audio codec (e.g., `.m4a` for AAC, `.mp3` for MP3).
- The tool auto-detects the audio codec to select the correct output format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
