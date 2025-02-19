import speech_recognition as sr
from pydub import AudioSegment

def transcribe_audio(file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    audio = AudioSegment.from_file(file_path)

    # Export the audio to a temporary WAV file
    temp_wav_path = "temp.wav"
    audio.export(temp_wav_path, format="wav")

    # Use the recognizer to transcribe the audio
    with sr.AudioFile(temp_wav_path) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"

if _name_ == "_main_":
    # Get user input for the audio file path
    audio_file_path = input("Please enter the path to the audio file (e.g., audio.wav): ")
    
    # Transcribe the audio
    transcription = transcribe_audio(audio_file_path)
    
    # Print the transcription
    print("Transcription:")
    print(transcription)
