import sys
from collections import deque

n,k = map(int,sys.stdin.readline().rstrip().split())
coins = list(set([int(sys.stdin.readline().rstrip()) for _ in range(n)]))

dp = [ 10001 for _ in range(k+1)]

dp[0] = 0

for i in range(len(coins)):
    coin = coins[i]
    for j in range(coins[i],k+1):
        dp[j] = min(dp[j],dp[j-coin]+1)

if dp[k] >= 10001:
    print(-1)
else:
    print(dp[k])