import sys
import bisect

for _ in range(int(sys.stdin.readline().rstrip())):
    
    coin_num = int(sys.stdin.readline().rstrip())
    coins = list(map(int,sys.stdin.readline().rstrip().split()))
    target = int(sys.stdin.readline().rstrip())
    
    dp = [[0 for _ in range(target+1)] for _ in range(len(coins))]
    
    for j in range(0,target+1,coins[0]):
        dp[0][j] = 1
    
    for i in range(1,coin_num):
        coin = coins[i]
        for j in range(0,target+1,coin):
            for k in range(0,target+1-j):
                dp[i][k+j] += dp[i-1][k]
            
    print(dp[-1][-1])