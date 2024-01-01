import os
import pickle


class PickleUtils:
    dirname: str

    def __init__(self, file):
        self.dirname = os.path.dirname(file)

    def read(self, name):
        return pickle.load(open(os.path.join(self.dirname, name), "rb"))
