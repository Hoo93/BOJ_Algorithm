import sys
from collections import deque
import heapq

INF = 10**8

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
instructions = sys.stdin.readlines()

size = int(instructions[0].rstrip())
num_list = sorted(map(int, instructions[1].rstrip().split()))
result = []

lidx, ridx, mn = 0, size - 1, 2000000001

while lidx < ridx:
    tmp = num_list[lidx] + num_list[ridx]

    if tmp == 0:
        result = [num_list[lidx], num_list[ridx]]
        break

    if abs(tmp) < mn:
        mn = abs(tmp)
        result = [num_list[lidx], num_list[ridx]]

    elif tmp < 0:
        lidx += 1
    else:
        ridx -= 1

print(" ".join(map(str, result)))
