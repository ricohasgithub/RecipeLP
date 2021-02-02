
from utils.models.heuristic_sequence import Heuristic_Sequence

n = [1, 2, 3, 4]
seq = Heuristic_Sequence(n)

for sublist in seq:
    print(sublist)

print("A wild success!")