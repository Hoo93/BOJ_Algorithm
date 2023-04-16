import sys
from collections import deque
import heapq

instructions = sys.stdin.readlines()

N, K = map(int, instructions[0].rstrip().split())
basket = [0 for _ in range(N + 1)]
for instruction in instructions[1:]:
    start, end, ball = map(int, instruction.rstrip().split())
    for i in range(start, end + 1):
        basket[i] = ball

print(" ".join(map(str, basket[1:])))
