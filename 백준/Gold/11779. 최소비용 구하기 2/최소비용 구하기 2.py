import sys
import heapq

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

INF = 10**9
graphs = [[] for _ in range(V + 1)]
visited = [INF for _ in range(V + 1)]
path = [0 for _ in range(V + 1)]


for _ in range(E):
    depart, arrive, cost = map(int, sys.stdin.readline().rstrip().split())
    graphs[depart].append((cost, arrive))

for graph in graphs:
    graph.sort()

start, end = map(int, sys.stdin.readline().rstrip().split())

hq = []
heapq.heappush(hq, (0, start, start))

while hq:
    cost, node, pre = heapq.heappop(hq)
    if cost >= visited[node]:
        continue
    visited[node] = cost
    path[node] = pre

    for dcost, n_node in graphs[node]:
        ncost = cost + dcost
        if visited[n_node] <= ncost:
            continue
        heapq.heappush(hq, (ncost, n_node, node))

print(visited[end])

result = [end]
while end != start:
    end = path[end]
    result.append(end)

print(len(result))
print(" ".join(map(str, result[::-1])))
