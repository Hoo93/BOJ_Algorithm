import sys
import heapq

vertex,edge = map(int,sys.stdin.readline().rstrip().split())
graphs = [ [] for _ in range(vertex+1)]

for _ in range(edge):
    n1,n2,dist = map(int,sys.stdin.readline().rstrip().split())
    graphs[n1].append((dist,n2))
    graphs[n2].append((dist,n1))

en1,en2 = map(int,sys.stdin.readline().rstrip().split())

def bfs(start,end):
    que = []
    visited = [ 10000000 for _ in range(vertex+1)]
    heapq.heappush(que,(0,start))
    while que:
        dist,node = heapq.heappop(que)
        if visited[node] <= dist: continue 
        visited[node] = dist
        for d,v in graphs[node]:
            if visited[v] <= dist+d: continue
            heapq.heappush(que,(dist+d,v))

    return visited[end]

result = bfs(1,en1) + bfs(en1,en2) + bfs(en2,vertex)
result = min(result,bfs(1,en2) + bfs(en2,en1) + bfs(en1,vertex))
if result >= 10000000: print(-1)
else: print(result)