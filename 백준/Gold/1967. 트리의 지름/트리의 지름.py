import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graphs = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(N - 1):
    parent, child, distance = map(int, sys.stdin.readline().rstrip().split())
    graphs[parent].append((child, distance))
    graphs[child].append((parent, distance))

que = deque()
que.append((1, 0))
far_node = 1
mx_dist = 0

while que:
    node, dist = que.popleft()
    if visited[node]:
        continue
    visited[node] = True
    if dist > mx_dist:
        far_node = node
        mx_dist = dist

    for v, d in graphs[node]:
        que.append((v, dist + d))

visited = [False for _ in range(N + 1)]
que = deque()
que.append((far_node, 0))
far_node = 1
mx_dist = 0

while que:
    node, dist = que.popleft()
    if visited[node]:
        continue
    visited[node] = True
    if dist > mx_dist:
        far_node = node
        mx_dist = dist

    for v, d in graphs[node]:
        que.append((v, dist + d))

print(mx_dist)
