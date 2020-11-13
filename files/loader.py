import csv
from abc import ABC, abstractmethod


class LoaderInterface(ABC):
    @property
    @abstractmethod
    def vocabulary(self):
        pass


class CSVLoader(LoaderInterface):
    def __init__(self, filename):
        self.filename = filename

    @property
    def vocabulary(self):
        with open(self.filename, "r") as file:
            file_reader = csv.reader(file)
            return {word: (meaning, example) for word, meaning, example in file_reader}
