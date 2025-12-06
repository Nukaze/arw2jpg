import rawpy
import imageio
from pathlib import Path

def process_image(file_path, output_folder, quality):
    """
    Core logic to convert a single ARW file to JPG.
    """
    try:
        # Define output filename
        filename = file_path.stem
        output_path = output_folder / f"{filename}.jpg"

        # Check if already exists (Skip feature)
        if output_path.exists():
            return {"status": "skipped", "path": str(output_path)}

        # Conversion Logic
        with rawpy.imread(str(file_path)) as raw:
            # Edit parameters here to change image look (brightness, gamma, etc)
            rgb = raw.postprocess(use_camera_wb=True, bright=1.0)
            
            # Save Image
            imageio.imsave(str(output_path), rgb, quality=quality, subsampling=0)
            
        return {"status": "success", "path": str(output_path)}

    except Exception as e:
        return {"status": "error", "file": file_path.name, "msg": str(e)}

def worker_wrapper(args):
    """
    Helper to unpack tuple arguments for multiprocessing.
    args: (file_path, output_folder, quality)
    """
    return process_image(*args)