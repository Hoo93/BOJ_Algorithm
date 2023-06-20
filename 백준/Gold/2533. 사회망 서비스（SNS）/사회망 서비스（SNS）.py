import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True

    for vertex in graphs[node]:
        if visited[vertex]:
            continue
        dfs(vertex)
        dp[node][1] += min(dp[vertex][0],dp[vertex][1])
        dp[node][0] += dp[vertex][1]

f = sys.stdin
# f = open("practice.txt",'r')

N = int(f.readline().rstrip())
graphs = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
# populations = [0] + list(map(int,f.readline().rstrip().split()))
dp = [[0,1] for i in range(N+1) ]

for _ in range(N-1):
    n1,n2 = map(int,f.readline().rstrip().split())
    graphs[n2].append(n1)
    graphs[n1].append(n2)

dfs(N//2+1)
print(min(dp[N//2+1]))