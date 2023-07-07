import sys
from itertools import permutations

f = sys.stdin
# f = open("input.txt","r")

N,M = map(int,f.readline().rstrip().split())
numList = sorted(map(int,f.readline().rstrip().split()))

for i in permutations(numList,M):
    print(" ".join(map(str,i)))