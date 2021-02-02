
from utils.models.naive_sequence import Naive_Sequence

class Heuristic_Sequence(Naive_Sequence):

    def __init__(self):
        super().__init__()
        
    def __init__(self, sequence):
        super().__init__(sequence)

    def tokenize(self):
        naive_tokens = super().naive_tokenize()
        return naive_tokens

    def train(self):
        pass

    def iterate(self):
        pass

    def operate(self):
        pass
