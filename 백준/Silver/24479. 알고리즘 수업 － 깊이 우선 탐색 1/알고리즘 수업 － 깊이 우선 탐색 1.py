import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

vertex,edge,start = map(int,input().rstrip().split())

graph = [[] for _ in range(vertex+1)]
visited = [False for _ in range(vertex+1)]
result = [ 0 for _ in range(vertex+1) ]
count = 0

for _ in range(edge):
    depart,arrive = map(int,input().rstrip().split())
    heapq.heappush(graph[depart],arrive)
    heapq.heappush(graph[arrive],depart)

def dfs(start):
    global count
    if not visited[start]:
        visited[start] = True
        count += 1
        result[start] = count

        while len(graph[start]):
            dfs(heapq.heappop(graph[start]))
        
dfs(start)

print("\n".join(map(str,result[1:])))