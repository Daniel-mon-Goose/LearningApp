from abc import ABC, abstractmethod


class LoaderInterface(ABC):
    def __init__(self, filename=""):
        self.filename = filename

    @classmethod
    @abstractmethod
    def load_words(cls):
        pass
