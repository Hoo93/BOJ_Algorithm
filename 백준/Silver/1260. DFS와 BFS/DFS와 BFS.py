import sys
from collections import deque
import heapq
input = sys.stdin.readline

node,edge,start_node = map(int,input().rstrip().split())

graph = [[] for _ in range(node+1)]
visited_dfs = [ False for _ in range(node+1)]
visited_bfs = [ False for _ in range(node+1)]

dfs_answer = []
bfs_answer = []

for _ in range(edge):
    start,end = map(int,input().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

for i in graph:
    i.sort()

def dfs(graph,node,visited_dfs):
    global dfs_answer
    if visited_dfs[node]:
        return
    else:
        dfs_answer.append(str(node))
        visited_dfs[node] = True
        for i in graph[node]:
            dfs(graph,i,visited_dfs)

que = deque()
que.append(start_node)
bfs_answer.append(str(start_node))
visited_bfs[start_node] = True

while que:
    vertex = que.popleft()
    for i in graph[vertex]:
        if not visited_bfs[i]:
            que.append(i)
            visited_bfs[i] = True
            bfs_answer.append(str(i))

dfs(graph,start_node,visited_dfs)
print(" ".join(dfs_answer))
print(" ".join(bfs_answer))