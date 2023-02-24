import sys

n,k = map(int,sys.stdin.readline().rstrip().split())

coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

dp = [ 0 for _ in range(k+1)]
dp[0] = 1
for i in range(1,k//coins[0]+1):
    dp[i*coins[0]] = 1
for i in range(1,n):
    for j in range(coins[i],k+1):
        dp[j] += dp[j-coins[i]]

print(dp[k])