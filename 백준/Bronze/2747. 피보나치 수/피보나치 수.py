dp = [0 for _ in range(46)]
dp[0] = 0
dp[1] = 1
for i in range(2,46):
    dp[i] = dp[i-2] + dp[i-1]
    
print(dp[int(input())])