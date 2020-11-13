import csv
from abc import ABC, abstractmethod

from tools.modifiers import format_check


class LoaderInterface(ABC):
    @property
    @abstractmethod
    def vocabulary(self):
        pass


class CSVLoader(LoaderInterface):
    def __init__(self, filename):
        self.filename = filename

    @property
    @format_check("filename", ".csv")
    def vocabulary(self):
        with open(self.filename, "r") as file:
            file_reader = csv.reader(file)
            return {word: (meaning, example) for word, meaning, example in file_reader}
