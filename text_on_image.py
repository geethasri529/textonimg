from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, output_path, position=(50, 50)):
    img = Image.open(image_path).convert("RGBA")

    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    # Use Times New Roman font from Windows fonts
    font = ImageFont.truetype("C:/Windows/Fonts/times.ttf", 15)

    draw.text(position, text, font=font, fill=(255, 255, 255, 255))

    combined = Image.alpha_composite(img, txt_layer)
    combined.save(output_path)

# Example usage
add_text_to_image("input.jpg", "This is your text!", "output.png")
