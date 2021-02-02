
from utils.abstract.sequences.naive_sequence import Naive_Sequence

class Heuristic_Sequence(Naive_Sequence):
        
    def __init__(self, sequence, model):
        super().__init__(sequence)
        self.model = model

    def tokenize(self):
        self.tokens = super().naive_tokenize()

    def train(self):
        pass

    def iterate(self):
        pass

    def operate(self):
        pass
