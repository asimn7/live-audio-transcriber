from record_audio import record_audio
from transcribe_audio import transcribe_audio

def main():
    audio_file = "live_audio.wav"
    
    # Step 1: Record Audio
    record_audio(audio_file, record_seconds=10)
    
    # Step 2: Transcribe Audio
    transcription = transcribe_audio(audio_file)
    print("Final Transcription:\n", transcription)

if __name__ == "__main__":
    main()
