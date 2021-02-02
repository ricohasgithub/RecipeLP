
import math

import utils.abstract.stratagem

class Naive_Sequence(Strategem):

    def __init__(self):
        super().__init__()

    def __init__(self, sequence):
        self.sequence = sequence
        self.tokens = []
    
    # Symbolic tokenization methods

    # Non-recursive implementation of a partition token generator (simple python sublist algorithm)
    def naive_tokenize(self):
        base = []   
        lists = [base] 
        for i in range(len(sequence)): 
            orig = lists[:] 
            new = sequence[i] 
            for j in range(len(lists)): 
                lists[j] = lists[j] + [new] 
            lists = orig + lists 
        return lists 
