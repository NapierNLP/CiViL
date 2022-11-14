import os
import pyaudio
import pyttsx3
import wave
import sys

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

from google.cloud import texttospeech

# setting Google credential
os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/carls/Downloads/turnkey-mender-362510-406e6c97578b.json"


def synthesize_text(text):
    """Synthesizes speech from the input string of text."""

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)


    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.say(text)  # play the speech
    engine.runAndWait()
    #response = client.synthesize_speech(
     #   request={"input": input_text, "voice": voice, "audio_config": audio_config}
    #)

    # The response's audio_content is binary.
    #with open("../output.wav", "wb") as out:
     #   out.write(response.audio_content)
      #  print('Audio content written to file "output.mp3"')

 #   CHUNK = 1024

 #   wf = wave.open("../output.wav", 'rb') # Original example
    #wf = response.audio_content

    # instantiate PyAudio (1)
 #   p = pyaudio.PyAudio()

    # open stream (2)
 #   stream = p.open(
  #      format=FORMAT,
   #                 channels=CHANNELS,
    #                rate=RATE,
     #               output=True)

    # read data
    #data = wf  # your_audio_data_array

    # play stream (3)
  #  while len(data) > 0:
   #     stream.write(data)
        # data = wf.readframes(CHUNK) # read more data if you want to stream another buffer

    # stop stream (4)
    #stream.stop_stream()
    #stream.close()

    # close PyAudio (5)
    #p.terminate()

if __name__ == "__main__":
    synthesize_text("You then have to place each of the slices onto a flattened out paper cupcake case on a baking tray, or into a greased muffin tin..")
