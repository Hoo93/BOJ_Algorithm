import sys
from collections import deque

vertex = int(sys.stdin.readline().rstrip())

graphs = [[] for _ in range(vertex + 1)]
visited = [0 for _ in range(vertex + 1)]
visited[1] = 1

for _ in range(vertex - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graphs[a].append(b)
    graphs[b].append(a)

que = deque()
que.append(1)

while que:
    root = que.popleft()

    for v in graphs[root]:
        if visited[v] > 0:
            continue
        visited[v] = root
        que.append(v)

for v in visited[2:]:
    print(v)
