from __future__ import annotations
from abc import ABC, abstractmethod

from vosk import Model, KaldiRecognizer
import pyaudio


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    def __init__(self):
        self._model = None
        self._recognizer = None
        self._mic = None
        self._stream = None
        self.recognised_text = None
        self._observers = []

    def set_model(self, module_path: str):
        self._model = Model(module_path)
        self._recognizer = KaldiRecognizer(self._model, 16000)

        self._mic = pyaudio.PyAudio()
        self._stream = self._mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                                      frames_per_buffer=8192)

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass
