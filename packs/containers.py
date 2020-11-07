from csv import reader


class CommonContainer:
    def __init__(self):
        self.data = {}

    def load_data(self, file_reader):
        pass


class CSVContainer(CommonContainer):
    def load_data(self, file_reader):
        self.data = {word: (meaning, example) for word, meaning, example in file_reader}
