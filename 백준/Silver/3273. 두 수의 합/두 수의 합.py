import sys
from collections import deque
import heapq

INF = 10**8

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
instructions = sys.stdin.readlines()

size = int(instructions[0].rstrip())
num_list = sorted(map(int, instructions[1].rstrip().split()))
target = int(int(instructions[2].rstrip()))
result = 0

lidx, ridx = 0, size - 1
while lidx < ridx:
    tmp = num_list[lidx] + num_list[ridx]
    if tmp == target:
        result += 1
        lidx += 1
        ridx -= 1
    elif tmp < target:
        lidx += 1
    else:
        ridx -= 1

print(result)
