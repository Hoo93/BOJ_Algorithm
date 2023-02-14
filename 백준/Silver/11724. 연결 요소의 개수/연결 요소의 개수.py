import sys
sys.setrecursionlimit(10**6)
vertex, edge = map(int,sys.stdin.readline().rstrip().split())

graphs = [ [] for _ in range(vertex+1)]
visited = [0 for _ in range(vertex+1)]

cnt = 0

for _ in range(edge):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    graphs[s].append(e)
    graphs[e].append(s)

def dfs(node):
    if visited[node]:
        return
    else:
        visited[node] = 1
        for v in graphs[node]:
            if visited[v]:
                continue
            else:
                dfs(v)

for i in range(1,vertex+1):
    if visited[i]:
        continue
    else:
        cnt += 1
        dfs(i)

print(cnt)