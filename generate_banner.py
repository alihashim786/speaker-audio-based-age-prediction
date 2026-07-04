"""
Generate GitHub Social Preview Banner
This script creates a 1280x640px PNG banner for GitHub repository social preview
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_banner():
    # Banner dimensions (GitHub social preview size)
    width, height = 1280, 640
    
    # Create image with gradient background
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # Create gradient background (purple-blue to deep purple)
    for y in range(height):
        # Calculate color gradient
        ratio = y / height
        r = int(102 + (118 - 102) * ratio)
        g = int(126 + (75 - 126) * ratio)
        b = int(234 + (162 - 234) * ratio)
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))
    
    # Try to load fonts, fallback to default if not available
    try:
        title_font = ImageFont.truetype("arial.ttf", 90)
        subtitle_font = ImageFont.truetype("arial.ttf", 40)
        feature_font = ImageFont.truetype("arial.ttf", 28)
        tech_font = ImageFont.truetype("arialbd.ttf", 24)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        feature_font = ImageFont.load_default()
        tech_font = ImageFont.load_default()
    
    # Add semi-transparent overlay for text readability
    overlay = Image.new('RGB', (width, height), (0, 0, 0))
    img = Image.blend(img, overlay, 0.1)
    draw = ImageDraw.Draw(img)
    
    # Draw microphone emoji/icon (as text)
    icon_text = "🎙️"
    draw.text((80, 80), icon_text, fill=(255, 255, 255), font=title_font)
    
    # Draw title
    title_y = 200
    draw.text((80, title_y), "Audio-Based", fill=(255, 255, 255), font=title_font)
    draw.text((80, title_y + 95), "Age Prediction", fill=(255, 255, 255), font=title_font)
    
    # Draw subtitle
    subtitle_y = title_y + 220
    draw.text((80, subtitle_y), "ML-Powered Speaker Classification System", 
              fill=(255, 255, 255, 240), font=subtitle_font)
    
    # Draw feature badges
    features_y = subtitle_y + 80
    features = [
        "📊 15,000+ Samples",
        "🔬 MFCC Features", 
        "🤖 ML Classification"
    ]
    
    feature_x = 80
    for feature in features:
        # Draw rounded rectangle background for badge
        bbox = draw.textbbox((0, 0), feature, font=feature_font)
        badge_width = bbox[2] - bbox[0] + 40
        badge_height = 50
        
        # Draw semi-transparent white background
        draw.rounded_rectangle(
            [(feature_x, features_y), (feature_x + badge_width, features_y + badge_height)],
            radius=25,
            fill=(255, 255, 255, 60)
        )
        
        # Draw text
        draw.text((feature_x + 20, features_y + 10), feature, 
                 fill=(255, 255, 255), font=feature_font)
        
        feature_x += badge_width + 20
    
    # Draw tech stack badges
    tech_y = features_y + 90
    tech_stack = ["Python", "Librosa", "Scikit-learn", "Pandas", "NumPy"]
    
    tech_x = 80
    for tech in tech_stack:
        bbox = draw.textbbox((0, 0), tech, font=tech_font)
        badge_width = bbox[2] - bbox[0] + 30
        badge_height = 40
        
        # Draw badge background
        draw.rounded_rectangle(
            [(tech_x, tech_y), (tech_x + badge_width, tech_y + badge_height)],
            radius=20,
            fill=(255, 255, 255, 80),
            outline=(255, 255, 255, 100),
            width=2
        )
        
        # Draw tech name
        draw.text((tech_x + 15, tech_y + 8), tech, 
                 fill=(255, 255, 255), font=tech_font)
        
        tech_x += badge_width + 15
    
    # Draw corner badges (top right)
    corner_badges = ["⭐ Open Source", "🎓 FAST NUCES"]
    badge_x = width - 80
    
    for badge_text in reversed(corner_badges):
        bbox = draw.textbbox((0, 0), badge_text, font=feature_font)
        badge_width = bbox[2] - bbox[0] + 40
        badge_height = 50
        badge_x -= badge_width + 20
        
        # Draw badge
        draw.rounded_rectangle(
            [(badge_x, 30), (badge_x + badge_width, 30 + badge_height)],
            radius=25,
            fill=(255, 255, 255, 80),
            outline=(255, 255, 255, 120),
            width=2
        )
        
        draw.text((badge_x + 20, 40), badge_text, 
                 fill=(255, 255, 255), font=feature_font)
    
    # Draw waveform bars at the bottom
    bar_width = 6
    bar_gap = 15
    num_bars = 40
    bar_start_x = (width - (num_bars * (bar_width + bar_gap))) // 2
    
    for i in range(num_bars):
        # Vary bar heights for visual effect
        bar_height = int(80 + 50 * ((i % 10) / 10))
        bar_x = bar_start_x + i * (bar_width + bar_gap)
        bar_y = height - bar_height - 20
        
        draw.rounded_rectangle(
            [(bar_x, bar_y), (bar_x + bar_width, height - 20)],
            radius=3,
            fill=(255, 255, 255, 50)
        )
    
    # Save the image
    output_path = "github-social-preview.png"
    img.save(output_path, 'PNG', quality=95)
    print(f"✅ Banner created successfully: {output_path}")
    print(f"📏 Dimensions: {width}x{height}px")
    print(f"📍 Location: {os.path.abspath(output_path)}")
    
    return output_path

if __name__ == "__main__":
    create_banner()
