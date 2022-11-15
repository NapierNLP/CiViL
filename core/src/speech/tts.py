import os
import pyaudio
import pyttsx3
import wave
import sys

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# from google.cloud import texttospeech

# setting Google credential
# os.environ[
#     'GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/carls/Downloads/turnkey-mender-362510-406e6c97578b.json"


def synthesize_text(text):
    """Synthesizes speech from the input string of text."""

    # client = texttospeech.TextToSpeechClient()
    #
    # input_text = texttospeech.SynthesisInput(text=text)
    #
    #
    # # Note: the voice can also be specified by name.
    # # Names of voices can be retrieved with client.list_voices().
    # voice = texttospeech.VoiceSelectionParams(
    #     language_code="en-US",
    #     name="en-US-Standard-C",
    #     ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    # )
    #
    # audio_config = texttospeech.AudioConfig(
    #     audio_encoding=texttospeech.AudioEncoding.MP3
    # )
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.say(text)  # play the speech
    engine.runAndWait()

if __name__ == "__main__":
    synthesize_text("You then have to place each of the slices onto a flattened out paper cupcake case on a baking tray, or into a greased muffin tin..")
