from abc import ABC, abstractmethod
import csv


class CommonContainer(ABC):
    def __init__(self):
        self.data = {}

    @abstractmethod
    def load_data(self, file_reader):
        pass


class CSVContainer(CommonContainer):
    def load_data(self, file_reader: csv.reader):
        self.data = {word: (meaning, example) for word, meaning, example in file_reader}
