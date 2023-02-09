import sys
from collections import deque

test_num = int(sys.stdin.readline().rstrip())

def bfs(graphs,visited):
    queue = deque()
    
    for i in range(1,len(graphs)):
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)
            while queue:
                node = queue.popleft()
                flag = visited[node]
        
                for v in graphs[node]:
                    if visited[v] == 0:
                        visited[v] = 3 - flag
                        queue.append(v)
                    elif visited[v] == flag:
                        return False
                    else:
                        continue
    return True

for _ in range(test_num):
    vertex,edge = map(int,sys.stdin.readline().rstrip().split())
    graphs = [ [] for _ in range(vertex+1)]
    visited = [ 0 for _ in range(vertex+1)]

    for _ in range(edge):
        start,end = map(int,sys.stdin.readline().rstrip().split())
        graphs[start].append(end)
        graphs[end].append(start)
    
    if bfs(graphs,visited):
        print("YES")
    else:
        print("NO")

    