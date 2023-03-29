import sys
from collections import deque
import heapq

INF = 10**8

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
instructions = sys.stdin.readlines()

vertices, edge = map(int, instructions[0].rstrip().split())
graphs = [[] for _ in range(vertices + 1)]
# 1. Distance와 Predecessor 생성
distance = [[INF for _ in range(vertices + 1)] for _ in range(vertices + 1)]

for instruction in instructions[1:]:
    depart, arrive, cost = map(int, instruction.rstrip().split())
    graphs[depart].append((arrive, cost))

for i in range(1, vertices + 1):
    distance[i][i] = 0
    for v, c in graphs[i]:
        distance[i][v] = c

for i in range(1, vertices + 1):
    for j in range(1, vertices + 1):
        for k in range(1, vertices + 1):
            if distance[j][k] > distance[j][i] + distance[i][k]:
                distance[j][k] = distance[j][i] + distance[i][k]

mn = INF

for i in range(1, vertices + 1):
    for j in range(i + 1, vertices + 1):
        mn = min(mn, distance[i][j] + distance[j][i])

if mn >= INF:
    print(-1)
else:
    print(mn)
