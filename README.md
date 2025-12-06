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

## 📂 Project Structure

```bash
arw2jpg/
├── arw2jpg.bat
├── requirements.txt
├── README.md
└── src/
    ├── __init__.py        # Package metadata (version, maintainer, license)
    ├── main.py            # Orchestrator (CLI & Progress Bar)
    ├── converter.py       # The Engine (Image Processing Logic)
    └── utils.py           # The Helper (Path & File Management)
```