import os
from PIL import Image, ImageDraw, ImageFont

# Dynamically find font file from Windows fonts folder
def get_font_path(font_name, font_dir="C:/Windows/Fonts/"):
    for font_file in os.listdir(font_dir):
        if font_name.lower() in font_file.lower() and font_file.lower().endswith(('.ttf', '.otf')):
            return os.path.join(font_dir, font_file)
    return None

def get_position_keyword(keyword, img_width, img_height, text_width, text_height):
    keyword = keyword.lower()
    if keyword == "center":
        return ((img_width - text_width) // 2, (img_height - text_height) // 2)
    elif keyword == "top":
        return ((img_width - text_width) // 2, 10)
    elif keyword == "bottom":
        return ((img_width - text_width) // 2, img_height - text_height - 10)
    elif keyword == "left":
        return (10, (img_height - text_height) // 2)
    elif keyword == "right":
        return (img_width - text_width - 10, (img_height - text_height) // 2)
    else:
        raise ValueError(f"Invalid position keyword: {keyword}")

def add_text_to_image(image_path, text, font_name, font_size, position, output_path):
    img = Image.open(image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    font_path = get_font_path(font_name)
    if not font_path:
        print(f"Font '{font_name}' not found. Using default font.")
        font_path = "C:/Windows/Fonts/times.ttf"

    font = ImageFont.truetype(font_path, font_size)

    # Get text size
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Determine position
    if isinstance(position, str) and position.lower() in ["center", "top", "bottom", "left", "right"]:
        position = get_position_keyword(position, img.width, img.height, text_width, text_height)
    elif isinstance(position, str) and "," in position:
        position = tuple(map(int, position.split(",")))
    else:
        raise ValueError("Invalid position input. Use 'center', 'top', 'bottom', 'left', 'right', or x,y format.")

    # Draw text
    draw.text(position, text, font=font, fill=(0, 0, 0, 255))

    combined = Image.alpha_composite(img, txt_layer)
    combined.save(output_path)

# --- User Inputs ---
image_path = input("Enter the image path (e.g., D:/tys/input.jpg): ").strip()
text = input("Enter the text to place on the image: ")
font_name = input("Enter the font name (e.g., 'Arial', 'Comic Sans MS'): ").strip()
font_size = int(input("Enter the font size (e.g., 30): "))
position_input = input("Enter the position (e.g., 'center', 'top', 'bottom', 'left', 'right', or x,y coordinates): ").strip()
output_path = "output111333.png"

# Call the function
add_text_to_image(image_path, text, font_name, font_size, position_input, output_path)
print(f"Image with text saved as {output_path}")
