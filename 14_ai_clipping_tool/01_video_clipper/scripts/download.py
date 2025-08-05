import os
import subprocess
import sys
import platform
import zipfile
import urllib.request

def ensure_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ FFmpeg is already installed.")
    except:
        print("⚠️ FFmpeg not found. Installing automatically...")
        if platform.system() == "Windows":
            ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
            zip_path = "ffmpeg.zip"
            extract_path = "C:\\ffmpeg"
            bin_path = os.path.join(extract_path, "ffmpeg-*-essentials_build", "bin")

            # Download the zip
            urllib.request.urlretrieve(ffmpeg_url, zip_path)
            print("📦 Downloaded FFmpeg ZIP.")

            # Extract
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            print("📂 Extracted FFmpeg to C:\\ffmpeg")

            # Detect correct subdir
            for root, dirs, _ in os.walk(extract_path):
                if 'ffmpeg.exe' in os.listdir(os.path.join(root, 'bin')):
                    ffmpeg_bin_path = os.path.join(root, 'bin')
                    break

            # Add to PATH temporarily
            os.environ["PATH"] += os.pathsep + ffmpeg_bin_path
            print(f"✅ FFmpeg installed and added to PATH: {ffmpeg_bin_path}")

            # Optionally, make it permanent:
            subprocess.run(f'setx /M PATH "%PATH%;{ffmpeg_bin_path}"', shell=True)
        else:
            print("❌ Auto install only supported on Windows. Please install FFmpeg manually.")

# Call this at the start of your pipeline
ensure_ffmpeg()
