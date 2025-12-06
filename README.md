# arw2jpg

A high-performance, multiprocessing tool to batch convert Sony RAW (`.ARW`) files to High-Quality JPEG images.

Designed for **Windows Drag-and-Drop** simplicity with engineer-grade logging and speed.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20linux-lightgrey)

---

## 🚀 Quick Start (For Users)

### Super Simple 3-Step Process

#### Step 1️⃣: Double-Click `arw2jpg.bat`
Find the `arw2jpg.bat` file in your project folder and double-click it.

#### Step 2️⃣: Drag Your Folder
When the window opens, **drag and drop** your folder (or single `.ARW` file) onto the window.

**You can drag:**
- 📁 A whole folder of `.ARW` files
- 📷 A single `.ARW` file

**OR** if drag-and-drop doesn't work, paste the full path and press Enter.

#### Step 3️⃣: Done!
Watch the progress bar! The output folder **opens automatically** when finished. ✨

### 📂 Where Are My Files?

Your converted JPEGs will be in a **new folder** created inside your source folder:

```
📁 Your Original Folder/
   📷 photo1.ARW
   📷 photo2.ARW
   📁 arw2jpg_2025-12-06/  ← NEW! (opens automatically)
      🖼️ photo1.jpg
      🖼️ photo2.jpg
```

### ✅ What You'll See

```
📂 Source: C:\Photos\vacation
🎯 Output: C:\Photos\vacation\arw2jpg_2025-12-06
📸 Count:  59 files
⚙️  CPU:    50% (6/12 Cores used)
----------------------------------------
100%|████████████████████| 59/59 [00:37<00:00, 1.56img/s]
----------------------------------------
✅ Processed: 59/59
⏱️  Time: 37.8s (avg 0.64s per image)

[System] Opening output folder...
```

### 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python is not recognized" | Install Python from [python.org](https://www.python.org) - check "Add to PATH" |
| "No ARW files found" | Make sure you selected the correct folder with `.ARW` files |
| Files already exist? | Already converted files are **skipped** automatically (faster!) |

---

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

---

# 🛠️ Developer Section

> **Note for Users:** Everything above is all you need to use the tool! The sections below are for developers who want to customize or understand the technical details.

---

## 💻 Command Line Usage (Advanced)

### Prerequisites
- Python 3.8 or higher
- Windows OS (for `.bat` launcher) or Linux/Mac (run Python directly)

### Manual Command Line

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