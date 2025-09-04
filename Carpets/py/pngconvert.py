import os
import json
import requests
from PIL import Image
from io import BytesIO

# Get the folder where THIS script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one level (Carpets/)
carpets_dir = os.path.dirname(script_dir)

# Path to your json folder
json_folder = os.path.join(carpets_dir, "json")

# Path to save PNG images
output_folder = os.path.join(carpets_dir, "images_png")
os.makedirs(output_folder, exist_ok=True)

print("📂 JSON folder:", json_folder)
print("📂 Output folder:", output_folder)

# Loop through all JSON files in /json
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):
        json_path = os.path.join(json_folder, filename)

        with open(json_path, "r") as f:
            data = json.load(f)

        # Iterate over products in JSON
        for item in data:
            if "image" in item and item["image"]:
                img_url = item["image"]

                try:
                    # Download image
                    if img_url.startswith("http"):
                        response = requests.get(img_url, timeout=10)
                        img = Image.open(BytesIO(response.content))
                    else:
                        # Local relative path case
                        local_path = os.path.join(carpets_dir, img_url.lstrip("/"))
                        img = Image.open(local_path)

                    # Ensure PNG
                    base_name = os.path.splitext(os.path.basename(img_url))[0]
                    png_name = base_name + ".png"
                    png_path = os.path.join(output_folder, png_name)

                    img.save(png_path, "PNG")

                    # Update JSON with new local PNG path
                    item["image"] = os.path.relpath(png_path, carpets_dir)

                except Exception as e:
                    print(f"❌ Failed for {img_url}: {e}")

        # Save updated JSON back
        with open(json_path, "w") as f:
            json.dump(data, f, indent=2)

        print(f"✅ Processed {filename}")