import argparse
import multiprocessing
import os
import math
import time
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

# Import our custom modules
import utils
import converter

def parse_arguments():
    parser = argparse.ArgumentParser(description="Modular ARW to JPG Converter")
    
    # Positional argument for input path (file or folder)
    parser.add_argument("path", help="Path to file or folder")
    
    # QUALITY SETTING EXPLANATION:
    # Default is 90. This is considered the "sweet spot" for JPEG compression.
    #
    # 1. VISUAL QUALITY:
    #    - >90 (95-100): Diminishing returns. Negligible visual improvement over 90.
    #    - <85: Risk of visible artifacts (mosquito noise) in high-contrast areas.
    #
    # 2. FILE SIZE (Approx for 24MP Image):
    #    - Quality 100: ~10-15 MB (Inefficient, near-lossless chroma)
    #    - Quality 90:  ~4-5 MB   (Best Balance)
    #    - Quality 80:  ~1-2 MB   (Good for web, bad for editing)
    parser.add_argument("--quality", "-q", type=int, default=90, help="JPG Quality")
    
    # add flag for unlocking CPU usage from default safe limit 80% of Logical Cores to 100%
    parser.add_argument("--unlock-cpu", action="store_true", help="Force use 100% of CPU cores (Warning: System may lag)")
    
    return parser.parse_args()


def calculate_workers(unlock_cpu_flag):
    """
    Algorithm to determine safe worker count.
    Default: 50% of Thread Cores (floor value).
    Unlock: 100% of Thread Cores.
    """
    total_cores = os.cpu_count() or 1 # Fallback to 1 if detection fails
    
    if unlock_cpu_flag:
        # User requested FULL POWER
        return total_cores
    else:
        # Default: 50% usage to keep OS responsive
        # Example: 12 cores * 0.5 = 6 -> 6 workers
        # Example: 4 cores * 0.5 = 2 -> 2 workers
        safe_count = math.floor(total_cores * 0.5)
        
        # return 1 # test
        return max(1, safe_count) # Ensure at least 1 worker


def main():
    # 1. Setup
    args = parse_arguments()
    
    # 2. Use Utils to find files
    files, base_dir = utils.get_input_files(args.path)
    
    if not files:
        print("⚠️ No ARW files found.")
        return

    # 3. Use Utils to make output folder
    output_dir = utils.create_output_dir(base_dir)

    # 4. Determine Workers
    max_workers = calculate_workers(args.unlock_cpu)
    total_cores = os.cpu_count()
    usage_percent = int((max_workers / total_cores) * 100)

    print(f"📂 Source: {base_dir}")
    print(f"🎯 Output: {output_dir}")
    print(f"📸 Count:  {len(files)}")
    print(f"⚙️  CPU:    {usage_percent}% ({max_workers}/{total_cores} Cores used)")
    if not args.unlock_cpu:
        print(f"    (Note: Use --unlock-cpu to use 100% power)")
    print("-" * 40)

    # 5. Prepare Data for Multiprocessing
    tasks = [(f, output_dir, args.quality) for f in files]

    success_count = 0
    errors = []

    # 6. Run the Engine (Converter)
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # We call the wrapper function in converter.py
        results = list(tqdm(executor.map(converter.worker_wrapper, tasks), total=len(tasks), unit="img"))

        for res in results:
            if res['status'] == 'success' or res['status'] == 'skipped':
                success_count += 1
            elif res['status'] == 'error':
                errors.append(f"{res['file']}: {res['msg']}")

    # 7. Final Report
    print("-" * 40)
    print(f"✅ Processed: {success_count}/{len(files)}")
    
    if errors:
        print("\n❌ Errors:")
        for err in errors:
            print(err)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()