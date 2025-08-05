import os
import sys
import subprocess
import hashlib
import json
from glob import glob
from scripts.download import download_video
from scripts.transcribe import transcribe_video

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

input_source = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=wJC6JWhpMwY"
is_youtube = input_source.startswith("http")

if is_youtube:
    print("📥 Downloading YouTube video...")
    download_dir = download_video(input_source)
    if not download_dir:
        sys.exit("❌ Download failed.")
    input_file = sorted(glob(os.path.join(download_dir, "*.mp4")))[0]
else:
    input_file = input_source

print("🧠 Summarizing video...")
result = subprocess.run(["python", "scripts/summarize.py", input_file], capture_output=True, text=True)
segments = json.loads(result.stdout.strip())

print("🎙️ Transcribing for captions...")
transcript = transcribe_video(input_file)

print("✂️ Creating final clip with captions...")
hash_id = hashlib.md5(input_source.encode()).hexdigest()
output_path = f"output/short_{hash_id}.mp4"

subprocess.run([
    "python", "scripts/create_clip.py",
    input_file, output_path, json.dumps(segments), json.dumps(transcript)
])

print(f"✅ Final clip saved to: {output_path}")
subprocess.run(f'explorer "{os.path.abspath("output")}"', shell=True)
