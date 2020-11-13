from abc import ABC, abstractmethod


class LoaderInterface(ABC):
    @staticmethod
    @abstractmethod
    def load_words(self, filename):
        pass
