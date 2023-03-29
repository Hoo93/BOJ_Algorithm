import sys
from collections import deque
import heapq

INF = 10**8

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
instructions = sys.stdin.readlines()

vertices, edge = map(int, instructions[0].rstrip().split())
graphs = []
distance = [INF for _ in range(vertices + 1)]
predecessor = [-1 for _ in range(vertices + 1)]
minus_cycle = False

for instruction in instructions[1:]:
    depart, arrive, cost = map(int, instruction.rstrip().split())
    graphs.append((depart, arrive, cost))

distance[1] = 0

for i in range(vertices - 1):
    for u, v, c in graphs:
        if distance[u] == INF:
            continue
        if distance[u] + c < distance[v]:
            distance[v] = distance[u] + c
            predecessor[v] = u


for u, v, c in graphs:
    if distance[u] == INF:
        continue
    if distance[u] + c < distance[v]:
        minus_cycle = True

if minus_cycle:
    print(-1)
else:
    for i in distance[2:]:
        if i >= INF:
            print(-1)
        else:
            print(i)
