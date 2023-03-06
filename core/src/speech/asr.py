import os.path
import string
from typing import List

from vosk import Model, KaldiRecognizer
import pyaudio

from observ_pattern import Subject


class CivilAsr(Subject):

    # def __int__(self,
    #             module_path=os.path.join(os.getcwd(), "data", "vosk-model-en-us-0.22-lgraph")):
    #     self.set_model(module_path)

    def set_new_model(self, module_path: str = os.path.join(os.getcwd(), "data", "vosk-model-en-us-0.22-lgraph")):
        self.set_model(module_path)

    def start(self):
        self._stream.start_stream()

        while True:
            data = self._stream.read(4096)

            if self._recognizer.AcceptWaveform(data):
                text = self._recognizer.Result()
                self.recognised_text = f"' {text[14:-3]} '"
                print(f"' {text[14:-3]} '")
                self.notify()
