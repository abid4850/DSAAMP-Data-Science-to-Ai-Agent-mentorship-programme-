import whisper

model = whisper.load_model("base")  # You can change to "small" or "medium"

def transcribe_video(file_path):
    result = model.transcribe(file_path)
    transcript = []
    for segment in result['segments']:
        transcript.append({
            "start": segment['start'],
            "end": segment['end'],
            "text": segment['text']
        })
    return transcript

if __name__ == "__main__":
    import sys, json
    if len(sys.argv) < 2:
        print("Usage: python scripts/transcribe.py <file_path>")
    else:
        output = transcribe_video(sys.argv[1])
        print(json.dumps(output))
