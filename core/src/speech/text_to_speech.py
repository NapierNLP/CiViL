import time
import pyttsx3


def synthesize_text(text):
    """Synthesizes speech from the input string of text."""

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.say(text)  # play the speech
    engine.runAndWait()

    time.sleep(1)


if __name__ == "__main__":
    # speak(
    #     "You then have to place each of the slices onto a flattened out paper cupcake case on a baking tray, or into a greased muffin tin..")
    synthesize_text(
        "You then have to place each of the slices onto a flattened out paper cupcake case on a baking tray, or into a greased muffin tin..")
