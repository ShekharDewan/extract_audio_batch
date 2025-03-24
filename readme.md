---

## ✅ `README.md`

```markdown
# Video to Audio Extractor (Original Quality)

This tool extracts the **original audio stream** from video files **without re-encoding**, preserving full audio quality. It uses `ffmpeg` to copy the audio stream directly and supports all major video formats. The tool automatically detects the correct audio format and saves the output to a separate folder.

---

## 🔧 Features

- ✅ Preserves original audio quality (no re-encoding)
- ✅ Detects correct audio format and sets proper file extension
- ✅ Processes all video files in a folder (batch mode)
- ✅ Skips files that were already extracted
- ✅ Works with all major video formats

---

## 📁 Folder Structure

```
video-to-audio-extractor/
├── extract_audio_batch.py         # Main script
├── README.md
├── LICENSE
├── .gitignore
├── input_videos/                  # Put your video files here
│   └── .gitkeep
└── output_audio/                  # Extracted audio files go here
    └── .gitkeep
```

---

## ▶️ How to Use

1. **Clone this repo** or download the project files.
2. Place your videos inside the `input_videos/` folder.
3. Run the script:

```bash
python extract_audio_batch.py
```

The script will process all video files in the `input_videos/` folder and save the extracted audio to the `output_audio/` folder using the same base filename, with `_audio` appended.

**Example:**

```
input_videos/my_clip.mp4 → output_audio/my_clip_audio.m4a
```

---

## 🧪 Supported Video Formats

- `.mp4`
- `.mov`
- `.mkv`
- `.avi`
- `.flv`
- `.webm`
- `.wmv`
- `.m4v`

---

## 📦 Dependencies

### Recommended: Conda (via conda-forge)

```bash
# Create environment
conda create -n video2audio python=3.10 -c conda-forge ffmpeg

# Activate environment
conda activate video2audio

# Install Python dependency
conda install -c conda-forge ffmpeg-python
```

### Alternatively: pip

```bash
# Requires ffmpeg installed system-wide
pip install ffmpeg-python
```

**Install ffmpeg on your system:**

- **macOS:** `brew install ffmpeg`
- **Ubuntu/Debian:** `sudo apt install ffmpeg`
- **Windows:** [Download and install](https://ffmpeg.org/download.html), and add `ffmpeg` to your system PATH

---

## ⚠️ Notes

- Audio is extracted **without re-encoding** for best quality (`-acodec copy`)
- Output filenames use the pattern `originalname_audio.extension`
- Output format depends on original audio codec (e.g., AAC → `.m4a`, MP3 → `.mp3`)

---

## 📝 License

MIT License. See [LICENSE](LICENSE) file for details.
```

---

## ✅ `LICENSE` (MIT License)

```text
MIT License

Copyright (c) 2025 Shekhar Dewan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```

---