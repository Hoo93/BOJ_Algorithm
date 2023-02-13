import sys
import bisect

num = int(sys.stdin.readline())

dp = [0 for _ in range(num+1)]

dp[0] = 1
dp[1] = 1

for i in range(2,num+1):
    dp[i] = (dp[i-1] +dp[i-2])%10007

print(dp[num])