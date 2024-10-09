import sys
import copy

vertex = int(sys.stdin.readline().rstrip())
INF = 10**8
graphs = [[INF for _ in range(vertex + 1)] for _ in range(vertex + 1)]

for _ in range(int(sys.stdin.readline().rstrip())):
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())
    if graphs[start][end] > cost:
        graphs[start][end] = cost

for k in range(1, vertex + 1):
    for i in range(1, vertex + 1):
        for j in range(1, vertex + 1):
            if j != i and graphs[i][j] > graphs[i][k] + graphs[k][j]:
                graphs[i][j] = graphs[i][k] + graphs[k][j]

for graph in graphs[1:]:
    for num in graph[1:]:
        if num == INF:
            print(0, end=" ")
        else:
            print(num, end=" ")
    print()
