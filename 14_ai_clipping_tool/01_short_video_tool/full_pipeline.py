import os
import sys
import subprocess
import json
from glob import glob

url = sys.argv[1]

# 1. Download
print("📥 Downloading...")
subprocess.run(["python", "scripts/download.py", url])
latest_file = sorted(glob("input/*"), key=os.path.getctime)[-1]

# 2. Transcribe & Select
print("🧠 Transcribing...")
result = subprocess.run(["python", "scripts/summarize.py", latest_file], capture_output=True)
segments = json.loads(result.stdout)

# 3. Cut Video
print("✂️ Creating clip...")
output_file = f"output/short_{os.path.basename(latest_file)}"
subprocess.run(["python", "scripts/create_clip.py", latest_file, output_file, json.dumps(segments)])

print(f"✅ Done! Final video saved at: {output_file}")
