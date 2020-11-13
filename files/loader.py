import csv
from abc import ABC, abstractmethod


class LoaderInterface(ABC):
    @abstractmethod
    def get_vocabulary(self, filename):
        pass


class CSVLoader(LoaderInterface):
    def get_vocabulary(self, filename):
        with open(filename, "r") as file:
            file_reader = csv.reader(file)
            return {word: (meaning, example) for word, meaning, example in file_reader}
