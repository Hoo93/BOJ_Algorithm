import sys
import heapq

INF = 10**9
vertex, edge = map(int,sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())
graphs = [ [] for _ in range(vertex+1)]
dist = [ INF for _ in range(vertex+1)]
dist[start] = 0

for _ in range(edge):
    s,e,w = map(int,sys.stdin.readline().rstrip().split())
    graphs[s].append((e,w))

que = []
heapq.heappush(que,(0,start))

while que:
    cost,point = heapq.heappop(que)
    if dist[point] < cost:
        continue

    for e,w in graphs[point]:
        ncost = cost + w
        if dist[e] <= ncost:
            continue
        dist[e] = ncost
        heapq.heappush(que,(ncost,e))
        
for i in range(1,vertex+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])