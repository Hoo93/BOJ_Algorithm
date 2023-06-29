import sys

# f = open("practice.txt","r")
f = sys.stdin

N = int(f.readline().rstrip())
costs = [ list(map(int,f.readline().rstrip().split())) for _ in range(N) ]
INF = 10**9

dp = [[-1 for _ in range(N)] for _ in range(1<<N)]

for i in range(1,N):
    if costs[i][0]:
        dp[(1<<N)-2][i] = costs[i][0]
    else:
        dp[(1<<N)-2][i] = INF

def dfs(now,pre):
    # if now == (1<<N) -1:
    #     if costs[pre][0] == 0:
    #         return 10**9
    #     else:
    #         return costs[pre][0]
    
    if dp[now][pre] != -1:
        return dp[now][pre]
    
    for i in range(1,N):
        if not costs[pre][i]:
            continue
            
        if now & 1<<i:
            continue
        
        if dp[now][pre] == -1:
            dp[now][pre] = dfs(now|1<<i,i) + costs[pre][i]
        else:
            dp[now][pre] = min(dp[now][pre], dfs(now|1<<i,i) + costs[pre][i])
            
    if dp[now][pre] == -1:
        return INF
    
    return dp[now][pre]


print(dfs(0,0))
