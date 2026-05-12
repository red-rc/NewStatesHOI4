from PIL import Image
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "provinces.bmp")

img = Image.open(file_path)
rgb = img.convert("RGB")

rgb.save(file_path, format="BMP")