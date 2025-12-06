import argparse
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

# Import our custom modules
import utils
import converter

def parse_arguments():
    parser = argparse.ArgumentParser(description="Modular ARW to JPG Converter")
    parser.add_argument("path", help="Path to file or folder")
    parser.add_argument("--quality", "-q", type=int, default=90, help="JPG Quality")
    return parser.parse_args()

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

    print(f"📂 Source: {base_dir}")
    print(f"🎯 Output: {output_dir}")
    print(f"📸 Count:  {len(files)}")
    print("-" * 40)

    # 4. Prepare Data for Multiprocessing
    # We pack arguments into tuples because map() only accepts one arg per worker
    tasks = [(f, output_dir, args.quality) for f in files]
    max_workers = multiprocessing.cpu_count()

    success_count = 0
    errors = []

    # 5. Run the Engine (Converter)
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # We call the wrapper function in converter.py
        results = list(tqdm(executor.map(converter.worker_wrapper, tasks), total=len(tasks), unit="img"))

        for res in results:
            if res['status'] == 'success' or res['status'] == 'skipped':
                success_count += 1
            elif res['status'] == 'error':
                errors.append(f"{res['file']}: {res['msg']}")

    # 6. Final Report
    print("-" * 40)
    print(f"✅ Processed: {success_count}/{len(files)}")
    
    if errors:
        print("\n❌ Errors:")
        for err in errors:
            print(err)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()