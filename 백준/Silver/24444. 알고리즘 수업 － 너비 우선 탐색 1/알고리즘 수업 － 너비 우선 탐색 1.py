import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

vertex,edge,start = map(int,input().rstrip().split())

graph = [[] for _ in range(vertex+1)]
visited = [False for _ in range(vertex+1)]
result = [ 0 for _ in range(vertex+1) ]
count = 0

que = deque()
que.append(start)

for _ in range(edge):
    depart,arrive = map(int,input().rstrip().split())
    heapq.heappush(graph[depart],arrive)
    heapq.heappush(graph[arrive],depart)

while que:
    v = que.popleft()
    if not visited[v]:
        visited[v] = True
        count += 1
        result[v] = count
    
        while graph[v]:
            que.append(heapq.heappop(graph[v]))
    
print("\n".join(map(str,result[1:])))