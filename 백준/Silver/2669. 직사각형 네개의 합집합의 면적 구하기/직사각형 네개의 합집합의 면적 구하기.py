import sys
from collections import deque

boards = [list(0 for i in range(100)) for i in range(100)]

for i in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            boards[j][i] = 1

print(sum(map(sum, boards)))
