import sys
import bisect

n,m = map(int,sys.stdin.readline().rstrip().split())

memories = list(map(int,sys.stdin.readline().rstrip().split()))
costs = list(map(int,sys.stdin.readline().rstrip().split()))

s = sum(costs)
dp = [0]*(s+1)

for i in range(n):
    cost = costs[i]
    memory = memories[i]
    for j in range(s,cost-1,-1):
        dp[j] = max(dp[j-cost]+memory,dp[j])

for i in range(s+1):
    if dp[i] >= m:
        print(i)
        break