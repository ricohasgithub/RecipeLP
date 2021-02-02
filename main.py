
from utils.models.heuristic_sequence import Heuristic_Sequence

n = [1, 2, 3, 4]
seq = Heuristic_Sequence(n)

seq.tokenize()

for sublist in seq:
    for token in sublist:
        print(token)

print("A wild success!")