import sys
from collections import deque

vertex = int(sys.stdin.readline().rstrip())
graphs = [[] for _ in range(vertex + 1)]

for _ in range(vertex):
    edges = list(map(int, sys.stdin.readline().rstrip().split()))
    v = edges[0]
    for i in range((len(edges) - 2) // 2):
        graphs[v].append(edges[2 * i + 1 : 2 * i + 3])


visited = [False for _ in range(vertex + 1)]
que = deque()
que.append((1, 0))
far = 0
far_node = 0
while que:
    node, distance = que.popleft()
    if visited[node]:
        continue
    visited[node] = True
    if distance > far:
        far = distance
        far_node = node
    for v, d in graphs[node]:
        que.append((v, distance + d))

visited = [False for _ in range(vertex + 1)]
que.clear()
que.append((far_node, 0))
far = 0
while que:
    node, distance = que.popleft()
    if visited[node]:
        continue
    visited[node] = True
    if distance > far:
        far = distance
        far_node = node
    for v, d in graphs[node]:
        que.append((v, distance + d))

print(far)
