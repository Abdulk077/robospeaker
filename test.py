import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

def save_and_play_tts(text, output_file='output.mp3'):
    engine = pyttsx3.init()

    # Save the TTS output as a WAV file
    engine.save_to_file(text, 'output.wav')
    engine.runAndWait()

    try:
        # Convert WAV to MP3 using pydub
        audio = AudioSegment.from_wav('output.wav')
        audio.export(output_file, format='mp3')

        # Play the saved MP3 file
        play(audio)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
text_to_speak = "Abdul."
save_and_play_tts(text_to_speak)