import string
from typing import List

from vosk import Model, KaldiRecognizer
import pyaudio

from observer import Observer
from subject import Subject


class SpeechRecogniser(Subject):

    def __int__(self, module_path=r"/home/yyu/Codebase/CiViL/core/src/data/vosk-model-en-us-0.22-lgraph"):
        self._recognised_text: string = None
        self._observers: List[Observer] = []

        self._model = Model(module_path)
        self._recognizer = KaldiRecognizer(self._model, 16000)

        self._mic = pyaudio.PyAudio()
        self._stream = self._mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def start(self):
        self._stream.start_stream()

        while True:
            data = self._stream.read(4096)

            if self._recognizer.AcceptWaveform(data):
                text = self._recognizer.Result()
                self._recognised_text = f"' {text[14:-3]} '"
                print(f"' {text[14:-3]} '")
                self.notify()

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)