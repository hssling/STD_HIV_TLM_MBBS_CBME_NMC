from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import random

def draw_simple_elements(draw, description, width, height):
    """Draw photorealistic visual elements based on keywords in the description"""
    desc_lower = description.lower()

    # Create advanced gradient background with atmospheric perspective
    for y in range(height):
        if y < height * 0.6:  # Sky with atmospheric scattering
            # Create realistic sky gradient with haze
            sky_factor = y / (height * 0.6)
            if 'night' in desc_lower or 'star' in desc_lower:
                # Night sky gradient
                r = int(25 + (70 - 25) * sky_factor)
                g = int(25 + (90 - 25) * sky_factor)
                b = int(112 + (150 - 112) * sky_factor)
            else:
                # Day sky gradient
                r = int(135 + (180 - 135) * sky_factor**0.8)
                g = int(206 + (235 - 206) * sky_factor**0.8)
                b = int(235 + (255 - 235) * sky_factor**0.8)
            draw.line([0, y, width, y], fill=(min(r, 255), min(g, 255), min(b, 255)))
        elif y < height * 0.8:  # Horizon haze
            haze_factor = (y - height * 0.6) / (height * 0.2)
            r = int(200 + (150 - 200) * haze_factor)
            g = int(220 + (120 - 220) * haze_factor)
            b = int(255 + (100 - 255) * haze_factor)
            draw.line([0, y, width, y], fill=(r, g, b))
        else:  # Ground with depth
            ground_factor = (y - height * 0.8) / (height * 0.2)
            if 'water' in desc_lower or 'river' in desc_lower or 'ocean' in desc_lower:
                # Water gradient
                r = int(0 + (50 - 0) * ground_factor)
                g = int(191 + (100 - 191) * ground_factor)
                b = int(255 + (150 - 255) * ground_factor)
            elif 'sand' in desc_lower or 'beach' in desc_lower:
                # Sand gradient
                r = int(238 + (194 - 238) * ground_factor)
                g = int(203 + (178 - 203) * ground_factor)
                b = int(173 + (128 - 173) * ground_factor)
            else:
                # Grass/ground gradient
                r = int(34 + (25 - 34) * ground_factor)
                g = int(139 + (100 - 139) * ground_factor)
                b = int(34 + (50 - 34) * ground_factor)
            draw.line([0, y, width, y], fill=(r, g, b))

    # Draw ground/floor with advanced texture
    if 'attic' in desc_lower or 'floor' in desc_lower or 'ground' in desc_lower:
        # Add dust particles and debris for attic
        if 'attic' in desc_lower:
            for i in range(50):
                x = random.randint(0, width)
                y = random.randint(height-150, height)
                draw.ellipse([x, y, x+2, y+2], fill=(169, 169, 169))

        # Wood grain texture for floors
        for i in range(0, width, 30):
            draw.line([i, height-120, i+15, height-115], fill=(101, 67, 33), width=3)
            draw.line([i+15, height-115, i+30, height-120], fill=(101, 67, 33), width=3)
            # Add knots and grain details
            if random.random() > 0.7:
                knot_x = i + random.randint(5, 25)
                draw.ellipse([knot_x-3, height-118, knot_x+3, height-112], fill=(71, 47, 23))

    # Draw detailed boxes with 3D effect
    if 'box' in desc_lower or 'chest' in desc_lower or 'attic' in desc_lower:
        for i in range(random.randint(3, 6)):
            x = random.randint(50, width-180)
            y = height - 180 - random.randint(0, 60)
            # Main box
            draw.rectangle([x, y, x+100, y+80], fill=(101, 67, 33), outline=(51, 25, 0), width=3)
            # 3D shadow effect
            draw.rectangle([x+5, y+5, x+105, y+85], fill=(71, 47, 23), outline=(51, 25, 0), width=1)
            # Lid
            draw.rectangle([x-2, y-10, x+102, y+5], fill=(81, 47, 23), outline=(51, 25, 0), width=2)

    # Draw detailed trees with layers
    if 'tree' in desc_lower or 'forest' in desc_lower:
        for i in range(random.randint(2, 5)):
            x = random.randint(80, width-120)
            trunk_height = random.randint(80, 120)
            # Trunk with bark texture
            draw.rectangle([x-15, height-trunk_height-100, x+15, height-100], fill=(139, 69, 19), outline=(101, 67, 33), width=2)
            # Bark lines
            for j in range(3):
                draw.line([x-10+j*7, height-trunk_height-90, x-10+j*7, height-110], fill=(101, 67, 33), width=3)

            # Multi-layer leaves
            leaf_colors = [(34, 139, 34), (50, 160, 50), (25, 120, 25)]
            for layer, color in enumerate(leaf_colors):
                size = 40 - layer * 8
                draw.ellipse([x-size, height-trunk_height-120+layer*15, x+size, height-trunk_height-40+layer*15], fill=color, outline=(20, 100, 20), width=1)

    # Draw animated water/river with waves
    if 'river' in desc_lower or 'water' in desc_lower or 'ocean' in desc_lower:
        # Base water
        draw.rectangle([0, height-180, width, height-80], fill=(0, 191, 255))
        # Wave patterns
        for i in range(0, width, 30):
            wave_y = height - 130 + random.randint(-10, 10)
            draw.arc([i, wave_y, i+30, wave_y+40], 0, 180, fill=(0, 150, 255), width=2)
        # Reflections/shimmer
        for i in range(15):
            x = random.randint(0, width)
            y = random.randint(height-170, height-90)
            draw.ellipse([x, y, x+3, y+6], fill=(255, 255, 255))

    # Draw fluffy clouds with shadows
    if 'sky' in desc_lower or 'cloud' in desc_lower:
        for i in range(random.randint(4, 10)):
            x = random.randint(0, width-120)
            y = random.randint(40, 250)
            # Main cloud
            draw.ellipse([x, y, x+100, y+60], fill=(240, 248, 255))
            draw.ellipse([x+20, y-10, x+80, y+50], fill=(240, 248, 255))
            draw.ellipse([x+40, y+10, x+90, y+70], fill=(240, 248, 255))
            # Shadow
            draw.ellipse([x+5, y+5, x+105, y+65], fill=(200, 220, 240), outline=(180, 200, 220))

    # Draw radiant sun with rays
    if 'sun' in desc_lower or 'sunlight' in desc_lower:
        center_x, center_y = width-100, 80
        # Sun rays
        for angle in range(0, 360, 30):
            import math
            ray_x = center_x + int(60 * math.cos(math.radians(angle)))
            ray_y = center_y + int(60 * math.sin(math.radians(angle)))
            draw.line([center_x, center_y, ray_x, ray_y], fill=(255, 255, 0), width=3)
        # Sun body with gradient effect
        draw.ellipse([center_x-40, center_y-40, center_x+40, center_y+40], fill=(255, 255, 0))
        draw.ellipse([center_x-35, center_y-35, center_x+35, center_y+35], fill=(255, 255, 100))
        draw.ellipse([center_x-25, center_y-25, center_x+25, center_y+25], fill=(255, 255, 150))

    # Draw twinkling stars
    if 'star' in desc_lower or 'night' in desc_lower:
        for i in range(25):
            x = random.randint(0, width)
            y = random.randint(0, height//2)
            # Star shape
            size = random.randint(3, 8)
            draw.ellipse([x-size//2, y-size//2, x+size//2, y+size//2], fill=(255, 255, 255))
            # Sparkle effect
            if size > 5:
                draw.ellipse([x-size, y, x+size, y+1], fill=(255, 255, 200))
                draw.ellipse([x, y-size, x+1, y+size], fill=(255, 255, 200))

    # Draw detailed cave with rocks
    if 'cave' in desc_lower:
        # Cave opening
        draw.ellipse([width//2-120, height//2-60, width//2+120, height//2+60], fill=(64, 64, 64))
        # Inner darkness
        draw.ellipse([width//2-100, height//2-40, width//2+100, height//2+40], fill=(32, 32, 32))
        # Rocks around entrance
        for i in range(8):
            angle = i * 45
            import math
            rock_x = width//2 + int(140 * math.cos(math.radians(angle)))
            rock_y = height//2 + int(80 * math.sin(math.radians(angle)))
            draw.ellipse([rock_x-15, rock_y-15, rock_x+15, rock_y+15], fill=(96, 96, 96), outline=(64, 64, 64))

    # Draw vibrant rainbow
    if 'rainbow' in desc_lower:
        colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
        for i, color in enumerate(colors):
            draw.arc([width//2-250, height//2-120+i*12, width//2+250, height//2+80+i*12], 0, 180, fill=color, width=12)

    # Draw beautiful flowers with details
    if 'flower' in desc_lower or 'garden' in desc_lower:
        for i in range(random.randint(6, 12)):
            x = random.randint(40, width-60)
            y = height - random.randint(120, 220)
            # Stem with leaves
            draw.rectangle([x-2, y, x+2, y+60], fill=(0, 128, 0))
            draw.ellipse([x-15, y+20, x+5, y+35], fill=(0, 100, 0))  # Leaf
            draw.ellipse([x-5, y+35, x+15, y+50], fill=(0, 100, 0))  # Leaf

            # Detailed flower
            petal_color = random.choice([(255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 0), (255, 165, 0)])
            # Petals
            for petal in range(6):
                import math
                angle = petal * 60
                petal_x = x + int(15 * math.cos(math.radians(angle)))
                petal_y = y + int(15 * math.sin(math.radians(angle)))
                draw.ellipse([petal_x-8, petal_y-8, petal_x+8, petal_y+8], fill=petal_color)
            # Center
            draw.ellipse([x-5, y-5, x+5, y+5], fill=(255, 255, 0))

    # Draw detailed dragon
    if 'dragon' in desc_lower:
        body_x, body_y = width//2, height//2
        # Scales on body
        draw.ellipse([body_x-60, body_y-35, body_x+60, body_y+35], fill=(0, 128, 0))
        for i in range(10):
            scale_x = body_x - 50 + i * 10
            draw.ellipse([scale_x-3, body_y-40, scale_x+3, body_y-30], fill=(0, 100, 0))

        # Detailed head
        draw.ellipse([body_x+40, body_y-50, body_x+90, body_y-10], fill=(0, 128, 0))
        # Eyes
        draw.ellipse([body_x+60, body_y-35, body_x+70, body_y-25], fill=(255, 255, 255))
        draw.ellipse([body_x+65, body_y-32, body_x+68, body_y-28], fill=(0, 0, 0))
        # Nostrils
        draw.ellipse([body_x+80, body_y-20, body_x+85, body_y-15], fill=(0, 0, 0))
        # Spikes
        for i in range(5):
            spike_x = body_x + 30 + i * 12
            draw.polygon([(spike_x, body_y-45), (spike_x+3, body_y-55), (spike_x+6, body_y-45)], fill=(0, 100, 0))

        # Wings with membrane
        wing_colors = [(0, 100, 0), (0, 80, 0)]
        for wing in [-1, 1]:
            wing_x = body_x + wing * 90
            # Wing bones
            draw.ellipse([wing_x-40, body_y-60, wing_x+40, body_y+10], fill=wing_colors[0])
            # Wing membrane
            draw.ellipse([wing_x-50, body_y-50, wing_x+50, body_y], fill=wing_colors[1])
            # Wing details
            for i in range(3):
                draw.line([wing_x-30+i*20, body_y-40, wing_x-20+i*20, body_y-20], fill=(0, 80, 0), width=2)

        # Tail
        draw.ellipse([body_x-90, body_y-20, body_x-30, body_y+10], fill=(0, 128, 0))
        # Tail spikes
        for i in range(4):
            spike_x = body_x - 80 + i * 15
            draw.polygon([(spike_x, body_y-25), (spike_x+2, body_y-35), (spike_x+4, body_y-25)], fill=(0, 100, 0))

    # Draw detailed birds
    if 'bird' in desc_lower or 'owl' in desc_lower:
        for i in range(random.randint(2, 4)):
            x = random.randint(80, width-120)
            y = random.randint(80, 350)
            is_owl = 'owl' in desc_lower and random.random() > 0.5

            # Body with feathers
            body_color = (20, 20, 20) if is_owl else (255, 255, 255)
            draw.ellipse([x-20, y-15, x+20, y+15], fill=body_color, outline=(0, 0, 0))

            # Wings with feather details
            wing_color = (10, 10, 10) if is_owl else (200, 200, 200)
            draw.ellipse([x-35, y-10, x-5, y+10], fill=wing_color, outline=(0, 0, 0))
            draw.ellipse([x+5, y-10, x+35, y+10], fill=wing_color, outline=(0, 0, 0))
            # Feather lines
            for j in range(3):
                draw.line([x-25+j*8, y-5, x-15+j*8, y+5], fill=(0, 0, 0), width=1)

            # Head
            draw.ellipse([x-12, y-25, x+12, y-5], fill=body_color, outline=(0, 0, 0))

            # Eyes
            eye_color = (255, 255, 0) if is_owl else (0, 0, 0)
            draw.ellipse([x-8, y-20, x-3, y-15], fill=eye_color)
            draw.ellipse([x+3, y-20, x+8, y-15], fill=eye_color)
            # Pupils
            draw.ellipse([x-6, y-18, x-5, y-17], fill=(0, 0, 0))
            draw.ellipse([x+5, y-18, x+6, y-17], fill=(0, 0, 0))

            # Beak
            beak_color = (255, 165, 0) if is_owl else (255, 255, 0)
            draw.polygon([(x-2, y-10), (x+2, y-10), (x, y-2)], fill=beak_color)

            # Legs
            draw.rectangle([x-8, y+15, x-5, y+25], fill=(255, 165, 0))
            draw.rectangle([x+5, y+15, x+8, y+25], fill=(255, 165, 0))

    # Draw detailed people (brothers)
    if 'boy' in desc_lower or 'brother' in desc_lower or 'child' in desc_lower or 'jathin' in desc_lower or 'kethan' in desc_lower:
        num_people = min(3, max(2, desc_lower.count('jathin') + desc_lower.count('kethan') + desc_lower.count('boy') + desc_lower.count('brother')))

        for i in range(num_people):
            x = 120 + i * 220
            y = height - 250

            # Clothes colors - blue for Jathin, red for Kethan
            shirt_color = (0, 0, 255) if i == 0 else (255, 0, 0)
            pants_color = (0, 0, 128) if i == 0 else (128, 0, 0)

            # Detailed head with hair
            draw.ellipse([x-15, y-15, x+15, y+15], fill=(255, 224, 189), outline=(200, 180, 150), width=2)
            # Hair
            hair_color = (139, 69, 19) if i == 0 else (0, 0, 0)  # Brown for Jathin, black for Kethan
            draw.ellipse([x-16, y-20, x+16, y-5], fill=hair_color)
            # Face details
            draw.ellipse([x-5, y-5, x-2, y-2], fill=(0, 0, 0))  # Left eye
            draw.ellipse([x+2, y-5, x+5, y-2], fill=(0, 0, 0))  # Right eye
            draw.arc([x-3, y+2, x+3, y+8], 0, 180, fill=(255, 100, 100), width=2)  # Smile

            # Shirt
            draw.rectangle([x-20, y+15, x+20, y+60], fill=shirt_color, outline=(0, 0, 0), width=2)
            # Sleeves
            draw.ellipse([x-30, y+20, x-10, y+40], fill=shirt_color, outline=(0, 0, 0))
            draw.ellipse([x+10, y+20, x+30, y+40], fill=shirt_color, outline=(0, 0, 0))

            # Pants
            draw.rectangle([x-15, y+60, x-5, y+100], fill=pants_color, outline=(0, 0, 0))
            draw.rectangle([x+5, y+60, x+15, y+100], fill=pants_color, outline=(0, 0, 0))

            # Shoes
            draw.ellipse([x-18, y+95, x-8, y+105], fill=(0, 0, 0))
            draw.ellipse([x+8, y+95, x+18, y+105], fill=(0, 0, 0))

            # Arms
            draw.ellipse([x-35, y+35, x-25, y+45], fill=(255, 224, 189), outline=(200, 180, 150))
            draw.ellipse([x+25, y+35, x+35, y+45], fill=(255, 224, 189), outline=(200, 180, 150))

            # Hands
            draw.ellipse([x-40, y+40, x-30, y+50], fill=(255, 224, 189), outline=(200, 180, 150))
            draw.ellipse([x+30, y+40, x+40, y+50], fill=(255, 224, 189), outline=(200, 180, 150))

    # Draw map if mentioned
    if 'map' in desc_lower:
        map_x, map_y = width//2 - 100, height//2 - 80
        # Map background
        draw.rectangle([map_x, map_y, map_x+200, map_y+160], fill=(210, 180, 140), outline=(139, 69, 19), width=3)
        # Map details - paths, landmarks
        draw.line([map_x+20, map_y+20, map_x+180, map_y+140], fill=(0, 100, 0), width=3)  # Path
        draw.ellipse([map_x+160, map_y+130, map_x+170, map_y+140], fill=(255, 0, 0))  # X mark
        draw.rectangle([map_x+50, map_y+60, map_x+80, map_y+90], fill=(0, 128, 0))  # Forest
        draw.ellipse([map_x+120, map_y+40, map_x+140, map_y+60], fill=(0, 191, 255))  # Lake
        # Compass rose
        draw.ellipse([map_x+100, map_y+80, map_x+110, map_y+90], fill=(0, 0, 0))
        draw.line([map_x+105, map_y+75, map_x+105, map_y+95], fill=(0, 0, 0), width=2)  # North
        draw.line([map_x+100, map_y+85, map_x+110, map_y+85], fill=(0, 0, 0), width=2)  # East-West

    # Draw castle/tower
    if 'castle' in desc_lower or 'tower' in desc_lower:
        castle_x = width//2 - 80
        castle_y = height - 300
        # Base
        draw.rectangle([castle_x, castle_y, castle_x+160, castle_y+200], fill=(169, 169, 169), outline=(105, 105, 105), width=3)
        # Towers
        draw.rectangle([castle_x-20, castle_y-50, castle_x+20, castle_y+50], fill=(169, 169, 169), outline=(105, 105, 105), width=2)
        draw.rectangle([castle_x+140, castle_y-50, castle_x+180, castle_y+50], fill=(169, 169, 169), outline=(105, 105, 105), width=2)
        # Windows
        for wx, wy in [(castle_x+30, castle_y+30), (castle_x+100, castle_y+30), (castle_x+30, castle_y+100), (castle_x+100, castle_y+100)]:
            draw.rectangle([wx, wy, wx+20, wy+30], fill=(135, 206, 235), outline=(0, 0, 0))
        # Door
        draw.rectangle([castle_x+60, castle_y+150, castle_x+100, castle_y+200], fill=(101, 67, 33), outline=(51, 25, 0), width=2)

    # Draw musical instruments
    if 'drum' in desc_lower or 'music' in desc_lower or 'instrument' in desc_lower:
        # Drums
        if 'drum' in desc_lower:
            drum_x, drum_y = width//2 - 60, height - 200
            draw.ellipse([drum_x, drum_y, drum_x+50, drum_y+40], fill=(139, 69, 19), outline=(101, 67, 33), width=3)
            draw.ellipse([drum_x+5, drum_y+5, drum_x+45, drum_y+35], fill=(210, 180, 140))
            # Drum sticks
            draw.line([drum_x-20, drum_y+20, drum_x+10, drum_y+20], fill=(101, 67, 33), width=4)
            draw.line([drum_x+40, drum_y+20, drum_x+70, drum_y+20], fill=(101, 67, 33), width=4)

        # Flute/bird calls
        if 'flute' in desc_lower or 'bird' in desc_lower:
            flute_x, flute_y = width//2 + 20, height - 220
            draw.rectangle([flute_x, flute_y, flute_x+80, flute_y+8], fill=(222, 184, 135), outline=(160, 82, 45))
            # Holes
            for i in range(6):
                draw.ellipse([flute_x+10+i*12, flute_y-2, flute_x+16+i*12, flute_y+10], fill=(160, 82, 45))

    # Draw clock/watch
    if 'clock' in desc_lower:
        clock_x, clock_y = width//2 - 40, height//2 - 40
        # Clock face
        draw.ellipse([clock_x, clock_y, clock_x+80, clock_y+80], fill=(255, 255, 255), outline=(0, 0, 0), width=4)
        # Numbers
        for i in range(12):
            import math
            angle = i * 30 - 90
            num_x = clock_x + 40 + int(30 * math.cos(math.radians(angle)))
            num_y = clock_y + 40 + int(30 * math.sin(math.radians(angle)))
            draw.text((num_x-3, num_y-5), str(i+1 if i>0 else 12), fill=(0, 0, 0), font=ImageFont.load_default())
        # Hands
        draw.line([clock_x+40, clock_y+40, clock_x+40, clock_y+20], fill=(0, 0, 0), width=3)  # Hour
        draw.line([clock_x+40, clock_y+40, clock_x+55, clock_y+40], fill=(255, 0, 0), width=2)  # Minute
        # Center dot
        draw.ellipse([clock_x+38, clock_y+38, clock_x+42, clock_y+42], fill=(0, 0, 0))

def create_illustration(description, filename, story_num, ill_num):
    # Create a colorful background
    colors = [
        (135, 206, 235),  # Sky blue
        (255, 182, 193),  # Light pink
        (144, 238, 144),  # Light green
        (255, 218, 185),  # Peach
        (221, 160, 221),  # Plum
        (176, 224, 230),  # Powder blue
        (255, 228, 196),  # Bisque
        (240, 230, 140),  # Khaki
        (255, 192, 203),  # Pink
        (173, 216, 230)   # Light blue
    ]

    # Choose color based on story number
    bg_color = colors[(story_num - 1) % len(colors)]

    # Create image
    img = Image.new('RGB', (800, 600), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Draw simple scene elements
    draw_simple_elements(draw, description, 800, 600)

    try:
        # Try to use a nice font
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        # Fallback to default
        font = ImageFont.load_default()

    # Add title
    title = f"Story {story_num} - Illustration {ill_num}"
    title_font = ImageFont.truetype("arial.ttf", 20) if os.path.exists("arial.ttf") else ImageFont.load_default()
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_x = (800 - (title_bbox[2] - title_bbox[0])) // 2
    draw.text((title_x, 20), title, fill='navy', font=title_font)

    # Add a small description box at the bottom
    desc_short = description[:100] + "..." if len(description) > 100 else description
    wrapped_desc = textwrap.fill(desc_short, width=60)
    desc_bbox = draw.textbbox((0, 0), wrapped_desc, font=font)
    desc_height = desc_bbox[3] - desc_bbox[0]
    draw.rectangle([10, 600-80, 790, 600-10], fill='white', outline='black')
    draw.text((20, 600-70), wrapped_desc, fill='black', font=font)

    # Save image
    img.save(filename)
    print(f"Created {filename}")

# Story illustrations data
illustrations = {
    1: [
        "A colorful illustration showing Jathin (a 10-year-old boy with brown hair and a curious smile) and Kethan (an 8-year-old boy with black hair and wide eyes) kneeling in a dusty attic. They're surrounded by old boxes and cobwebs. Jathin is holding up an ancient-looking map with a big red X marking a spot. Kethan looks excited, pointing at the map. Sunlight streams through a small window, creating golden beams.",
        "A vibrant scene of the brothers crossing a clear blue river on stepping stones. Jathin leads the way, testing each stone carefully. Kethan follows, holding a stick like a walking staff. Colorful fish swim in the water below, and dragonflies hover in the air. The forest on the other side looks mysterious and inviting.",
        "The boys standing in front of a large moss-covered stone with ancient writing carved into it. Jathin is reading the riddle aloud, scratching his head thoughtfully. Kethan is looking around for clues, pointing at different objects in the forest. Trees surround them, and birds are perched on branches watching curiously.",
        "A joyful scene at the top of the hill where the brothers have dug up a wooden chest. The chest is open, revealing not gold coins, but old family photos, letters, and small trinkets. Jathin and Kethan are hugging each other, smiling widely. The sunset paints the sky in orange and pink hues behind them."
    ],
    2: [
        "A magical forest scene with tall trees, glowing mushrooms, and sparkling streams. Jathin and Kethan are walking hand-in-hand along a path, looking curious. In the background, there's a large cave entrance with smoke gently rising from it. The sky is twilight blue with stars beginning to appear.",
        "The boys entering the cave cautiously. The dragon is curled up on a bed of soft moss, looking surprised but friendly. His wings are folded, and there's a small pile of shiny rocks nearby. Jathin is holding out his hand in greeting, while Kethan hides slightly behind his brother but peeks out curiously.",
        "A fun scene inside the cave where the boys are playing tag with Ember. The dragon is trying to catch them gently with his tail, laughing. There are drawings on the cave walls showing their games, and some fruits and berries scattered around as snacks. The atmosphere is warm and joyful.",
        "An exciting outdoor scene at dusk. Ember is standing on a small hill, spreading his wings tentatively. Jathin and Kethan are cheering him on from below, holding hands. The dragon's wings catch the wind, and he's starting to lift off the ground. Fireflies dance around them, and the moon is rising in the background."
    ],
    3: [
        "A beautiful forest edge with sunlight filtering through leaves. Jathin and Kethan are standing at the entrance of a narrow path between two ancient trees that form an arch. The trees have friendly faces carved into their bark. Butterflies and birds surround them, and there's a small sign that says 'Welcome to the Magical Forest.'",
        "A lively clearing where various animals are gathered. A wise old owl perches on a branch, a family of rabbits hop around, squirrels chatter from trees, and a deer watches curiously. Jathin and Kethan are in the center, looking amazed. Flowers are blooming in bright colors, and there's a small pond with fish jumping.",
        "A grand scene in a circle of ancient trees. The trees have faces and are gathered in a council. Jathin and Kethan are sitting on toadstools, listening intently. The animals are also present, sitting around. One tree is speaking, with leaves rustling like it's talking. Sunbeams filter through the canopy.",
        "A magical nighttime scene where all the forest inhabitants are gathered. Trees are glowing softly, animals are dancing, flowers are sparkling. Jathin and Kethan are holding hands, singing along. Fireflies light up the air like floating lanterns, and stars twinkle above. The atmosphere is peaceful and joyful."
    ],
    4: [
        "A cozy bedroom scene with toys scattered around. Jathin and Kethan are opening an old wooden wardrobe in their room. Inside, instead of clothes, there are glowing capes hanging on hooks - one red for Jathin, one blue for Kethan. The capes shimmer with superhero symbols, and there's a soft magical light emanating from them.",
        "An outdoor backyard scene where the boys are practicing their powers. Jathin is wearing the red cape, pretending to fly by jumping high. Kethan in blue cape is running super fast in circles. Their dog is watching curiously, and there are superhero poses and action lines drawn in the air. The sun is shining brightly.",
        "A busy town street scene. An elderly lady's groceries are falling from her bag. Jathin (in red cape) is catching the items mid-air with super strength. Kethan (in blue cape) is helping organize them back. Shopkeepers and townspeople are watching in amazement. The sky is clear and sunny.",
        "A dramatic scene at the town park. A little girl is stuck high in a tree, crying. Jathin is climbing the tree with super strength, reaching for her. Kethan is below, directing and encouraging. The girl's parents are worried below, and other children are watching. Birds are flying around, and leaves are falling."
    ],
    5: [
        "An attic scene cluttered with old boxes and treasures. Jathin and Kethan are exploring, and Kethan has just uncovered a beautiful antique clock covered in dust. The clock has strange symbols and glowing hands. Sunlight streams through a window, highlighting the clock's magical glow.",
        "A prehistoric landscape with volcanoes in the background and lush ferns. Jathin and Kethan are hiding behind a rock, watching dinosaurs roam. There's a friendly-looking stegosaurus munching on leaves nearby, and pterodactyls flying in the sky. The boys look both scared and excited.",
        "A futuristic cityscape with flying cars, tall skyscrapers with holographic ads, and robots walking on streets. Jathin and Kethan are standing on a platform, looking amazed. People are wearing shiny clothes, and there are floating gardens in the air. The sky is filled with colorful lights.",
        "Back in the attic, the clock is ticking normally. Jathin and Kethan are sitting on the floor, looking thoughtful. They're holding a notebook where they've drawn pictures of what they saw. The attic looks peaceful, with the clock glowing softly on a shelf."
    ],
    6: [
        "A sunny beach scene with waves crashing gently. Jathin and Kethan are playing in the sand, building sandcastles. Kethan finds a large, glowing seashell half-buried in the sand. The shell has a pearl inside that shines with rainbow colors. Seagulls fly overhead, and the ocean sparkles in the background.",
        "An underwater scene where the boys are swimming with fish. They've transformed to have fish-like features - gills on their necks and webbed hands. Colorful coral reefs surround them, and various fish swim by. Jathin is pointing at a school of fish, while Kethan is laughing with bubbles around him.",
        "A grand underwater palace made of coral and pearls. Various sea creatures are gathered - octopuses, turtles, seahorses, and a mermaid princess. Jathin and Kethan are meeting the mermaid, who has flowing hair and a crown of shells. The palace has glowing crystals and bubbles floating around.",
        "An exciting scene exploring a sunken shipwreck. The boys are swimming through the wreck, finding treasure chests and old artifacts. Fish are swimming in and out of the ship, and there's a giant clam with a pearl. Jathin is holding up an old compass, while Kethan is playing with a school of fish."
    ],
    7: [
        "A beautiful sky scene with fluffy white clouds and a rainbow arching across. Jathin and Kethan are standing on a hill, looking up at the sky. A magical ladder made of rainbow colors extends from the ground up into the clouds. Butterflies are flying around, and there's a gentle breeze blowing their hair.",
        "Inside the cloud castle's grand hall. Fluffy cloud creatures with friendly faces are welcoming the boys. There are cloud bunnies hopping around, cloud birds flying, and a wise cloud king with a crown made of lightning. The hall is filled with floating bubbles and gentle mist.",
        "A magical workshop inside the castle where weather is created. Jathin and Kethan are helping mix ingredients in giant cauldrons. There are bottles of sunshine, jars of rain, containers of wind, and baskets of snowflakes. Nimbus is supervising, and cloud helpers are bringing ingredients.",
        "An exciting scene flying on cloud chariots pulled by cloud horses. Jathin and Kethan are riding through the sky, waving at birds and looking down at the world below. The chariots are made of fluffy clouds with rainbow reins. Stars are beginning to appear as evening falls."
    ],
    8: [
        "A sunny meadow filled with wildflowers and tall grass. Jathin and Kethan are walking through it when they hear beautiful music. Various animals are gathered - a lion with a drum, a bird with a flute, a frog with a violin. The animals are playing instruments made from natural objects, and there's a conductor owl on a tree stump.",
        "A close-up scene of the boys meeting the animal musicians. Each animal is showing their instrument: a cricket with tiny cymbals, a beaver with a xylophone made of wood, an elephant with a tuba made from a large leaf. Jathin is trying a small drum, while Kethan is listening to the bird's flute. The atmosphere is friendly and musical.",
        "A practice session in the meadow. The boys are learning instruments - Jathin is trying the drums, Kethan is attempting the flute. Animals are teaching them patiently. There are sheet music floating in the air (made of leaves), and everyone is laughing and having fun. Sunbeams filter through the trees.",
        "A spectacular concert scene at sunset. All the animals and boys are performing on a natural stage with flowers and trees as decorations. The audience includes other forest creatures - squirrels, rabbits, deer. Fireflies provide lighting, and the music notes are visualized as colorful swirls in the air. Everyone looks happy and proud."
    ],
    9: [
        "A clear night sky filled with twinkling stars. Jathin and Kethan are lying on a blanket in their backyard, stargazing. A bright shooting star streaks across the sky, leaving a trail of sparkling light. The boys look amazed and excited, pointing at the star. Fireflies glow around them.",
        "The boys waking up to find a glowing star-shaped pendant on their pillows. The pendant has a soft light and seems to pulse with energy. Their room is filled with morning light, and they're looking at the pendant curiously. The window shows the sunrise outside.",
        "A series of small scenes showing the boys having adventures. Jathin is exploring a forest trail with a map, finding hidden paths. Kethan is helping neighbors - carrying groceries for an elderly lady, planting flowers in the community garden. The Wish Stones are glowing on their necks.",
        "A heartwarming scene where the boys are sharing their experiences. They're sitting under the same night sky, looking at the stars. The Wish Stones are glowing brightly. Jathin is telling an adventure story, Kethan is showing a drawing of helping others. The star from the beginning is visible in the sky."
    ],
    10: [
        "A lush garden with overgrown vines and flowers. Jathin and Kethan are standing in front of an old stone wall with a hidden gate covered in ivy. The gate has a dreamcatcher symbol carved into it. Butterflies and birds surround them, and there's a soft magical glow emanating from behind the gate.",
        "Inside the garden, flowers of every color bloom, each representing different dreams. Jathin is touching a flower that shows adventure scenes, Kethan is near flowers showing helping others. Dream bubbles float in the air showing various scenes. A wise gardener figure made of light welcomes them.",
        "The boys planting dream seeds in the garden soil. Jathin is planting an adventure seed that sprouts immediately into a tiny tree with map leaves. Kethan is planting a kindness seed that blooms into flowers with smiling faces. The Dream Keeper is guiding them, and dream bubbles show what their dreams will become.",
        "A magical scene where the garden's dreams are manifesting. The boys are experiencing their dreams - Jathin is on a gentle adventure finding small treasures, Kethan is helping garden creatures. Dream bubbles are becoming reality around them. The garden is vibrant and full of life, with the Dream Keeper smiling approvingly."
    ]
}

# Create images directory
os.makedirs('images', exist_ok=True)

# Generate all images
for story_num in range(1, 11):
    for ill_num in range(1, 5):
        description = illustrations[story_num][ill_num - 1]
        filename = f'images/story{story_num}_illustration{ill_num}.png'
        create_illustration(description, filename, story_num, ill_num)

print("All illustration images have been created!")
