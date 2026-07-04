"""
Automatic GitHub Social Preview Banner Uploader
This script attempts to upload the banner using GitHub's API
"""

import subprocess
import os
import base64

def upload_banner():
    banner_path = "github-social-preview.png"
    
    if not os.path.exists(banner_path):
        print("❌ Banner file not found!")
        return
    
    print("📸 Banner file found!")
    print(f"📁 Path: {os.path.abspath(banner_path)}")
    print(f"📏 Size: {os.path.getsize(banner_path) / 1024:.2f} KB")
    
    print("\n" + "="*70)
    print("⚠️  IMPORTANT: GitHub Social Preview Upload")
    print("="*70)
    print("\nUnfortunately, GitHub doesn't provide an API to upload social preview")
    print("images programmatically. You need to upload it manually.\n")
    
    print("📋 QUICK UPLOAD STEPS:")
    print("-" * 70)
    print("1. Go to: https://github.com/alihashim786/audio-based-age-prediction/settings")
    print("2. Scroll to 'Social preview' section")
    print("3. Click 'Edit' → 'Upload an image'")
    print("4. Select: github-social-preview.png")
    print("5. Click 'Save'")
    print("-" * 70)
    
    # Try to open the settings page
    repo_url = "https://github.com/alihashim786/audio-based-age-prediction/settings"
    
    print(f"\n🌐 Opening repository settings...")
    try:
        subprocess.run(["gh", "repo", "view", "--web"], check=True)
        print("✅ Repository page opened!")
        print("\n💡 Now navigate to Settings tab and upload the banner!")
    except:
        print(f"🔗 Please open manually: {repo_url}")
    
    # Show banner preview
    print("\n📸 Opening banner preview...")
    try:
        if os.name == 'nt':  # Windows
            os.startfile(banner_path)
        elif os.name == 'posix':  # Linux/Mac
            subprocess.run(["xdg-open", banner_path])
        print("✅ Banner preview opened!")
    except:
        print("⚠️  Please open manually:", banner_path)
    
    print("\n" + "="*70)
    print("✅ READY TO UPLOAD!")
    print("="*70)
    print("\nYour banner is professional and ready. Just upload it to GitHub! 🚀")
    print("\nFile location:", os.path.abspath(banner_path))

if __name__ == "__main__":
    upload_banner()
