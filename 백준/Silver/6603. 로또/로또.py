import sys
from itertools import combinations

#f = open("practice.txt", "r")
#instructions = f.readlines()
instructions = sys.stdin.readlines()

for instruction in instructions[: len(instructions) - 1]:
    nlt = list(map(int, instruction.rstrip().split()[1:]))

    for i in combinations(nlt, 6):
        print(" ".join(map(str, i)))
    
    print()
