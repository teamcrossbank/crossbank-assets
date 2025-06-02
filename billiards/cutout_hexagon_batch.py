# cutout_hexagon_batch.py
# Applies a vertical hexagon cutout to all JPG images in the folder where this script resides

import os
from PIL import Image, ImageDraw

def apply_hexagon_cutout(image_path, output_path):
    image = Image.open(image_path).convert("RGB")
    width, height = image.size

    # Create vertical hexagon mask
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    hexagon = [
        (width // 2, 0),
        (width, height // 4),
        (width, 3 * height // 4),
        (width // 2, height),
        (0, 3 * height // 4),
        (0, height // 4)
    ]
    draw.polygon(hexagon, fill=255)

    result = Image.new("RGB", (width, height), (255, 255, 255))
    result.paste(image, mask=mask)
    result.save(output_path)

def main():
    folder = os.getcwd()
    for filename in os.listdir(folder):
        if filename.lower().endswith(".jpg") and not filename.startswith("cutout_"):
            input_path = os.path.join(folder, filename)
            output_filename = f"cutout_{filename}"
            output_path = os.path.join(folder, output_filename)
            apply_hexagon_cutout(input_path, output_path)
            print(f"✅ Processed: {filename} -> {output_filename}")

if __name__ == "__main__":
    main()

