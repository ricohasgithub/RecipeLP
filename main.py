
from utils.abstract.sequences.heuristic_sequence import Heuristic_Sequence

n = [1, 2, 3, 4]
seq = Heuristic_Sequence(n, [])

seq.tokenize()

for sublist in seq.tokens:
    print(sublist)

print("A wild success!")