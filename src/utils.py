import sys
from pathlib import Path
from datetime import datetime

def get_input_files(raw_input_path):
    """
    Analyzes input path and returns:
    1. List of .ARW files found
    2. The base directory for output
    """
    path = Path(raw_input_path).resolve()
    
    if not path.exists():
        print(f"❌ Error: Path not found: {path}")
        sys.exit(1)

    files = []
    base_dir = None

    if path.is_file():
        # User provided a single file
        if path.suffix.lower() not in ['.arw']:
            print("❌ Error: Input is not an .ARW file.")
            sys.exit(1)
        files = [path]
        base_dir = path.parent

    elif path.is_dir():
        # User provided a folder
        files = list(path.glob("*.[aA][rR][wW]"))
        base_dir = path

    return files, base_dir

def create_output_dir(base_dir):
    """
    Creates a dated folder inside the base_dir.
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_path = base_dir / f"arw2jpg_{date_str}"
    output_path.mkdir(exist_ok=True)
    return output_path