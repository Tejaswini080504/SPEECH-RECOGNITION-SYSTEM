# SPEECH-RECOGNITION-SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TEJASWINI MADDIRALA

*INTERN ID*: CT12QRY

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH

# DESCRIPTION
tHE code is designed to transcribe speech from an audio file (in various formats) into text.
It performs the following steps:

Load and Convert Audio File:
The code uses pydub to load audio files in different formats and converts them to WAV format, which is necessary for speech recognition.

Speech Recognition:
It utilizes the speech_recognition library (with the Google Web Speech API) to transcribe the speech from the converted audio into text.
If the speech is intelligible, it will return the transcribed text; otherwise, it handles errors gracefully.

Error Handling:
The code includes error handling to manage situations where the speech cannot be understood (UnknownValueError) or when there are issues with the Google Web Speech API request (RequestError).

Components:
transcribe_audio(file_path)
Input: Takes the file path of an audio file (e.g., MP3, WAV) as input.
Process:
Initializes the speech recognizer.
Loads the audio using pydub, converts it to WAV, and exports it to a temporary file.
Reads the audio data and uses Google’s Web Speech API for recognition.

Output: Returns the transcribed text or an error message if transcription fails.

Main Program Block:
The main program prompts the user to input the path to an audio file.
It then calls the transcribe_audio() function and prints the transcription.

Applicable Use Case:
This script is useful for applications where you need to transcribe speech from an audio file to text, such as:
Converting recorded interviews, meetings, or podcasts to text.
Generating captions or subtitles for videos.
Transcribing voice memos or dictations.

Key Libraries:
speech_recognition: Handles the speech recognition task, specifically using the Google Web Speech API to convert audio to text.
pydub: A powerful audio manipulation library used here to handle audio format conversion (from non-WAV formats to WAV, which is compatible with the speech recognition library).

How to Run:
Install necessary libraries (if not already installed):pip install SpeechRecognition pydub
Make sure that ffmpeg (used by pydub for audio conversion) is installed on your machine.
Run the Python script and enter the path to the audio file when prompted.
The script will output the transcription of the audio.

# OUTPUT:

