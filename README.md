# arw2jpg

A high-performance, multiprocessing tool to batch convert Sony RAW (`.ARW`) files to High-Quality JPEG images. 

Designed for **Windows Drag-and-Drop** simplicity with engineer-grade logging and speed.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20linux-lightgrey)

## ⚡ Features

* **Zero-Config Usage:** Just drag a folder or file onto `arw2jpg.bat`.
* **Auto-Dependency Installation:** First run automatically installs required Python packages.
* **Auto-Organization:** Creates a clean, date-stamped output folder (e.g., `arw2jpg_2025-12-06`) inside the source directory.
* **Multiprocessing:** Uses 50% of CPU cores by default (configurable with `--unlock-cpu` for 100% power).
* **Smart Skipping:** Checks if the output JPG already exists to prevent redundant processing.
* **Processing Time Tracking:** Shows total conversion time and average time per image.
* **Auto-Open Output:** Automatically opens the output folder when conversion completes.
* **Quality Control:** Adjustable JPEG quality (1-100, default 90) with validation.
* **Path with Spaces Support:** Handles Windows paths containing spaces correctly.
* **Sony Optimized:** Uses `libraw` (via `rawpy`) for accurate "As Shot" white balance and color rendering.
* **UTF-8 Support:** Works correctly on all Windows locales (including Thai, Japanese, etc.).

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Windows OS (for drag-and-drop `.bat` launcher)

### Usage

**Method 1: Drag and Drop (Recommended)**
1. Drag a folder or `.ARW` file onto `arw2jpg.bat`
2. Dependencies auto-install on first run
3. Watch the progress bar
4. Output folder opens automatically when done!

**Method 2: Command Line**
```bash
# Basic usage (default quality 90, 50% CPU)
python src/main.py "C:\path\to\arw\files"

# Custom quality
python src/main.py "C:\path\to\arw\files" --quality 95

# Use 100% CPU power
python src/main.py "C:\path\to\arw\files" --unlock-cpu

# Combine options
python src/main.py "C:\path\to\arw\files" --quality 85 --unlock-cpu
```

### Output Example
```
📂 Source: C:\Photos\vacation_2024
🎯 Output: C:\Photos\vacation_2024\arw2jpg_2025-12-06
📸 Count:  59
⚙️  CPU:    50% (6/12 Cores used)
    (Note: Use --unlock-cpu to use 100% power)
----------------------------------------
100%|████████████████████| 59/59 [00:37<00:00,  1.56img/s]
----------------------------------------
✅ Processed: 59/59
⏱️  Time: 37.8s (avg 0.64s per image)
```

---

## 📂 Project Structure

```bash
arw2jpg/
├── arw2jpg.bat        # Windows launcher with auto-dependency install
├── requirements.txt   # Python dependencies (rawpy, imageio, tqdm)
├── README.md
└── src/
    ├── __init__.py        # Package metadata (version, maintainer, license)
    ├── main.py            # Orchestrator (CLI & Progress Bar)
    ├── converter.py       # The Engine (Image Processing Logic)
    └── utils.py           # The Helper (Path & File Management)
```

---

## 🛠️ Advanced Options

| Option | Description | Default |
|--------|-------------|---------|
| `--quality`, `-q` | JPEG quality (1-100) | 90 |
| `--unlock-cpu` | Use 100% of CPU cores | 50% |

### Quality Guide
- **100**: Maximum quality (~10-15 MB per image, minimal compression)
- **90**: Recommended sweet spot (~4-5 MB, excellent quality)
- **80**: Good for web (~1-2 MB, visible compression artifacts)

---

## 🧪 Testing

All bug fixes have been tested:
- ✅ Quality validation (rejects values outside 1-100)
- ✅ Path with spaces handling
- ✅ Return dictionary consistency
- ✅ Package metadata accessibility

---

## 📝 Version History

**v1.0.0** (2025-12-06)
- Initial release
- Multiprocessing support with CPU control
- Auto-dependency installation
- Processing time tracking
- Auto-open output folder
- Quality validation (1-100 range)
- UTF-8 console support for international locales
- Path with spaces support

---

## 👥 Contributors

- **Nukaze** - Main developer and maintainer
- **Claude Code (Anthropic AI)** - Development assistance

---

## 📄 License

MIT License - see LICENSE file for details