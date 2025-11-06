from PIL import Image, ImageDraw, ImageFont
import os

def create_logo():
    """Create a simple logo for the story book"""
    # Create a 200x200 image with a gradient background
    img = Image.new('RGB', (200, 200), color='#FF6B6B')
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fallback to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 24)
        small_font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Draw a simple book icon
    draw.rectangle([50, 50, 150, 150], fill='#FFFFFF', outline='#333333', width=2)
    draw.rectangle([60, 60, 140, 140], fill='#F8F8F8')
    # Book pages
    draw.line([70, 70, 70, 130], fill='#E0E0E0', width=8)
    draw.line([80, 70, 80, 130], fill='#E0E0E0', width=8)
    draw.line([90, 70, 90, 130], fill='#E0E0E0', width=8)

    # Add text
    draw.text((100, 170), "J&K", fill='#FFFFFF', font=font, anchor='mm')
    draw.text((100, 185), "Stories", fill='#FFFFFF', font=small_font, anchor='mm')

    img.save('assets/logo.png')
    print("Logo created: assets/logo.png")

def create_banner():
    """Create a banner for social media"""
    # Create a 1200x400 banner
    img = Image.new('RGB', (1200, 400), color='#667EEA')
    draw = ImageDraw.Draw(img)

    # Add gradient effect
    for y in range(400):
        r = int(102 + (255-102) * (y/400))
        g = int(126 + (107-126) * (y/400))
        b = int(234 + (0-234) * (y/400))
        draw.line([0, y, 1200, y], fill=(r, g, b))

    # Try to use fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 48)
        subtitle_font = ImageFont.truetype("arial.ttf", 24)
        small_font = ImageFont.truetype("arial.ttf", 18)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Add text
    draw.text((600, 150), "🌟 Jathin and Kethan Story Book 🌟", fill='#FFFFFF', font=title_font, anchor='mm')
    draw.text((600, 200), "10 Magical Adventures for Young Dreamers", fill='#FFFFFF', font=subtitle_font, anchor='mm')
    draw.text((600, 250), "Featuring Brothers Jathin (10) and Kethan (8)", fill='#FFFFFF', font=small_font, anchor='mm')
    draw.text((600, 300), "✨ Interactive Stories • Beautiful Illustrations • Valuable Lessons ✨", fill='#FFFFFF', font=small_font, anchor='mm')

    # Add some decorative elements
    draw.ellipse([50, 50, 150, 150], fill='#FFFFFF', outline='#FF6B6B', width=3)
    draw.ellipse([1050, 250, 1150, 350], fill='#FFFFFF', outline='#FF6B6B', width=3)

    img.save('assets/banner.png')
    print("Banner created: assets/banner.png")

def create_social_card():
    """Create a social media card"""
    img = Image.new('RGB', (1200, 630), color='#FF6B6B')
    draw = ImageDraw.Draw(img)

    # Add gradient
    for y in range(630):
        r = int(255 - (255-102) * (y/630))
        g = int(107 + (126-107) * (y/630))
        b = int(107 + (234-107) * (y/630))
        draw.line([0, y, 1200, y], fill=(r, g, b))

    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        subtitle_font = ImageFont.truetype("arial.ttf", 30)
        body_font = ImageFont.truetype("arial.ttf", 24)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    # Add content
    draw.text((600, 200), "🌟 Jathin & Kethan 🌟", fill='#FFFFFF', font=title_font, anchor='mm')
    draw.text((600, 280), "Illustrated Story Book", fill='#FFFFFF', font=subtitle_font, anchor='mm')
    draw.text((600, 340), "10 Magical Adventures • Interactive Reading • Beautiful Art", fill='#FFFFFF', font=body_font, anchor='mm')
    draw.text((600, 400), "Perfect for Young Dreamers Ages 5-12", fill='#FFFFFF', font=body_font, anchor='mm')
    draw.text((600, 500), "📚 Available on GitHub • 🌐 Streamlit App • 📄 PDF Download", fill='#FFFFFF', font=body_font, anchor='mm')

    img.save('assets/social_card.png')
    print("Social card created: assets/social_card.png")

if __name__ == "__main__":
    os.makedirs('assets', exist_ok=True)
    create_logo()
    create_banner()
    create_social_card()
    print("All assets created successfully!")
