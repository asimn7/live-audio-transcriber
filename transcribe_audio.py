import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("small")  # or 'small', 'medium', 'large'
    result = model.transcribe(audio_path)
    print("Transcription: ", result["text"])
    return result["text"]