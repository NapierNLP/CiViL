import time
import pyttsx3


def synthesize_text(text):
    """Synthesizes speech from the input string of text."""

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 128)  # Speed percent (can go over 100)
    engine.setProperty('volume', 1)  # Volume 0-1
    engine.say(text)  # play the speech
    engine.runAndWait()


    time.sleep(0.5)


if __name__ == "__main__":
    # speak(
    #     "You then have to place each of the slices onto a flattened out paper cupcake case on a baking tray, or into a greased muffin tin..")
    synthesize_text(
        "Hello, my name is Euclid what meal would you like me to help you cook today.")
