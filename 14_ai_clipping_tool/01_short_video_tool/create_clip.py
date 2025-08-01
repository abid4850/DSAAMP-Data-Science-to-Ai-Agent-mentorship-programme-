from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys
import json

def create_summary(input_path, output_path, segments):
    video = VideoFileClip(input_path)
    clips = [video.subclip(start, end) for start, end in segments]
    final = concatenate_videoclips(clips)
    final = final.resize(height=1920, width=1080)  # Vertical TikTok format
    final.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    segments = json.loads(sys.argv[3])
    create_summary(input_path, output_path, segments)
