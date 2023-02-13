import sys
import bisect

n,m = map(int,sys.stdin.readline().rstrip().split())

memories =[0]+ list(map(int,sys.stdin.readline().rstrip().split()))
costs =[0]+ list(map(int,sys.stdin.readline().rstrip().split()))
INF = 1e8
length = sum(costs)+1
dp = [ [0 for _ in range(length)] for _ in range(n+1)]

for i in range(1,n+1):
    memory = memories[i]
    cost = costs[i]

    for j in range(length-1,cost-1,-1):
        dp[i][j] = max(dp[i-1][j-cost]+memory,dp[i-1][j])
    for j in range(cost):
        dp[i][j] = dp[i-1][j]

print(bisect.bisect_left(dp[n],m))