import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0,0,1,1,2,3,2,3,3,2,3] + [0]*1000000

for i in range(11,n+1):
    if i%3 == 0 and i%2 == 0 :
        dp[i] = min(dp[i//3] + 1,dp[i//2]+1)
    elif i%3 == 0 :
        dp[i] = min(dp[i//3]+1,dp[i-1]+1,dp[i-2]+2)
    elif i%2 == 0 :
        dp[i] = min(dp[i//2]+1,dp[i-1]+1,dp[i-2]+2)
    else:
        dp[i] = min(dp[i-1]+1,dp[i-2]+2)

print(dp[n])