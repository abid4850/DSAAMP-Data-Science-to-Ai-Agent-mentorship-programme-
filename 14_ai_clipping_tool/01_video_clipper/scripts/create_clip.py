import sys
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
from PIL import Image

if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS

def add_captions(base_clip, transcript):
    subtitles = []
    for segment in transcript:
        txt = TextClip(segment["text"], fontsize=50, color='white', font="Arial-Bold", bg_color="black")
        txt = txt.set_start(segment["start"]).set_end(segment["end"])
        txt = txt.set_position(("center", "bottom"))
        subtitles.append(txt)
    return CompositeVideoClip([base_clip, *subtitles])

def create_summary(input_path, output_path, segments, transcript):
    clips = [VideoFileClip(input_path).subclip(start, end) for start, end in segments]
    final = concatenate_videoclips(clips)
    final = final.resize(height=1920)
    final = final.crop(x_center=final.w // 2, width=1080)

    final = add_captions(final, transcript)
    final.write_videofile(output_path, codec="libx264", audio_codec="aac", remove_temp=True)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python scripts/create_clip.py <input_path> <output_path> <segments_json> <transcript_json>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    segments = json.loads(sys.argv[3])
    transcript = json.loads(sys.argv[4])
    create_summary(input_path, output_path, segments, transcript)
