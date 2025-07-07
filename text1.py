import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

def get_font_path(font_name, font_dir="C:/Windows/Fonts/"):
    for file in os.listdir(font_dir):
        if font_name.lower() in file.lower() and file.lower().endswith(('.ttf', '.otf')):
            return os.path.join(font_dir, file)
    return None

def get_position(text_type, img_size, text_size):
    img_w, img_h = img_size
    txt_w, txt_h = text_size
    if text_type == "title":
        return ((img_w - txt_w) // 2, 10)
    elif text_type == "phone":
        return (img_w - txt_w - 10, img_h - txt_h - 10)
    elif text_type == "discount":
        return ((img_w - txt_w) // 2, (img_h - txt_h) // 2)
    return (0, 0)

def add_texts(image_path, texts_info, output_path):
    img = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    for text_type, info in texts_info.items():
        content = info["text"].strip()
        if content:
            font_name = info["font"]
            font_size = info["size"]
            color_name = info["color"]

            font_path = get_font_path(font_name)
            if not font_path:
                print(f"Font '{font_name}' not found. Using Times New Roman.")
                font_path = "C:/Windows/Fonts/times.ttf"

            try:
                font_color = ImageColor.getrgb(color_name)
            except ValueError:
                print(f"Invalid color '{color_name}'. Using black.")
                font_color = (0, 0, 0)

            font = ImageFont.truetype(font_path, font_size)
            bbox = draw.textbbox((0, 0), content, font=font)
            w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            pos = get_position(text_type, img.size, (w, h))

            draw.text(pos, content, font=font, fill=font_color + (255,))

    final_img = Image.alpha_composite(img, overlay)
    final_img.save(output_path)
    print(f"\n✅ Image with styled texts saved as {output_path}")

# === INPUT SECTION ===
image_path = input("Enter the image path (e.g., D:/tys/input.jpg): ").strip()

texts_info = {}
for text_type in ["title", "phone", "discount"]:
    content = input(f"\nEnter {text_type} text (or leave blank): ").strip()
    if content:
        font_name = input(f"Enter font name for {text_type} (e.g., Arial, Segoe UI): ").strip()
        font_size = int(input(f"Enter font size for {text_type} (e.g., 40): "))
        font_color = input(f"Enter font color for {text_type} (e.g., red, blue): ").strip().lower()
        texts_info[text_type] = {
            "text": content,
            "font": font_name,
            "size": font_size,
            "color": font_color
        }

output_path = "output666666666.png"
add_texts(image_path, texts_info, output_path)
