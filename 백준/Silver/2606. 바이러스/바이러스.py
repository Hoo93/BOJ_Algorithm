import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

vertex = int(sys.stdin.readline().rstrip())
edge = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(vertex+1)]
visited = [False for _ in range(vertex+1)]
count = 0

que = deque()
que.append(1)

for _ in range(edge):
    depart,arrive = map(int,input().rstrip().split())
    heapq.heappush(graph[depart],-1*arrive)
    heapq.heappush(graph[arrive],-1*depart)

while que:
    v = que.popleft()
    if not visited[v]:
        visited[v] = True
        count += 1
    
        while graph[v]:
            que.append(-1*heapq.heappop(graph[v]))
    
print(count-1)