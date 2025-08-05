import sys
import json
from moviepy.editor import VideoFileClip

def summarize_video(input_path):
    video = VideoFileClip(input_path)
    duration = int(video.duration)
    segments = [[0, min(duration, 30)]]  # Just first 30 seconds
    video.close()
    return segments

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/summarize.py <input_video_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    segments = summarize_video(input_path)
    print(json.dumps(segments))
