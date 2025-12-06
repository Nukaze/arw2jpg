"""
arw2jpg - Sony ARW to JPEG Converter

A high-performance, multiprocessing tool to batch convert Sony RAW (.ARW)
files to High-Quality JPEG images.

Features:
- Drag-and-drop Windows interface
- Automatic dependency installation
- Parallel processing with CPU control
- Smart skip logic for existing files
- Real-time progress tracking
- Auto-open output folder
"""

__version__ = "1.0.0"
__maintainer__ = ["Nukaze"]
__contributors__ = ["Nukaze", "Claude Code (Anthropic AI)"]
__license__ = "MIT"
__status__ = "Production"

# Note: Relative imports don't work when main.py is run directly as a script.
# This __init__.py file exists to:
# 1. Make 'src' a proper Python package
# 2. Provide version metadata
# 3. Enable future package-style imports if needed
