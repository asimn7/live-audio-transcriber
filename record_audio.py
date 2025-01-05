import pyaudio
import wave

def record_audio(output_filename="live_audio.wav", record_seconds=10, rate=44100, chunk=1024):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

