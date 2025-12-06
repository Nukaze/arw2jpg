# arw2jpg

A high-performance, multiprocessing tool to batch convert Sony RAW (`.ARW`) files to High-Quality JPEG images. 

Designed for **Windows Drag-and-Drop** simplicity with engineer-grade logging and speed.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20linux-lightgrey)

## ⚡ Features

* **Zero-Config Usage:** Just drag a folder or file onto `main.bat`.
* **Auto-Organization:** Creates a clean, date-stamped output folder (e.g., `arw2jpg_2025-12-06`) inside the source directory.
* **Multiprocessing:** Automatically detects CPU cores and parallelizes the conversion (approx. 4-10x faster than standard scripts).
* **Smart Skipping:** Checks if the output JPG already exists to prevent redundant processing.
* **Sony Optimized:** Uses `libraw` (via `rawpy`) for accurate "As Shot" white balance and color rendering.

## 📂 Project Structure

```bash
arw2jpg/
├── arw2jpg.bat
├── requirements.txt
├── README.md
└── src/
    ├── __init__.py        # (Empty file, makes 'src' a package)
    ├── main.py            # Orchestrator (CLI & Progress Bar)
    ├── converter.py       # The Engine (Image Processing Logic)
    └── utils.py           # The Helper (Path & File Management)
```