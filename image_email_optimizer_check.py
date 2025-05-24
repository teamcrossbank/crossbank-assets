# image_email_optimizer_check.py
# Script to optimize all PNG files in the 'lifestyle' folder for email use and save to 'web'

import os
from PIL import Image

MAX_WIDTH = 800
MAX_SIZE_KB = 300
INPUT_DIR = "lifestyle"
OUTPUT_DIR = "web"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def optimize_image(path, out_dir):
    try:
        with Image.open(path) as img:
            width, height = img.size
            filename = os.path.basename(path)
            name, _ = os.path.splitext(filename)

            # Resize if necessary
            if width > MAX_WIDTH:
                ratio = MAX_WIDTH / width
                new_size = (MAX_WIDTH, int(height * ratio))
                img = img.resize(new_size, Image.LANCZOS)
            else:
                new_size = (width, height)

            output_path = os.path.join(out_dir, name + ".png")
            img.save(output_path, optimize=True)

            new_size_kb = os.path.getsize(output_path) / 1024
            return {
                'original': path,
                'optimized': output_path,
                'original_size_kb': int(os.path.getsize(path) / 1024),
                'optimized_size_kb': int(new_size_kb),
                'original_width': width,
                'new_width': new_size[0]
            }
    except Exception as e:
        return {'path': path, 'error': str(e)}

def optimize_lifestyle_folder():
    report = []
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".png"):
            full_path = os.path.join(INPUT_DIR, file)
            result = optimize_image(full_path, OUTPUT_DIR)
            report.append(result)
    return report

def main():
    results = optimize_lifestyle_folder()
    print("\nLifestyle Image Optimization Report:\n")
    for entry in results:
        if 'error' in entry:
            print(f"ERROR: {entry['path']} - {entry['error']}")
        else:
            print(f"Optimized {entry['original']} -> {entry['optimized']} ({entry['original_size_kb']}KB → {entry['optimized_size_kb']}KB, width {entry['original_width']} → {entry['new_width']})")
    print("\nAll lifestyle images processed.")

if __name__ == "__main__":
    main()

