import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
nlt = sorted(map(int, sys.stdin.readline().split()))

result = 0

for i in range(1, N + 1):
    for j in combinations(nlt, i):
        if sum(j) == S:
            result += 1

print(result)
