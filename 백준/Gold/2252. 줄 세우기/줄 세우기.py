import sys
import heapq
from collections import deque

f = sys.stdin

N,M = map(int,f.readline().rstrip().split())
graph = [ [] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
queue = deque()
result = []

for _ in range(M):
    n1,n2 = map(int,f.readline().rstrip().split())
    graph[n1].append(n2)
    degree[n2] += 1

for i in range(1,N+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    result.append(node)
    for v in graph[node]:
        degree[v] -= 1
        if degree[v] == 0:
            queue.append(v)

print(" ".join(map(str,result)))

    




