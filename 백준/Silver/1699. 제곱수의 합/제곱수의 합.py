import sys
import math

num = int(sys.stdin.readline().rstrip())

dp = [0,1,2,3,1] + [10**6 for _ in range(num)]

if num <= 4:
    print(dp[num])
else:
    for i in range(5,num+1):
        for j in range(2,int(math.sqrt(i))+1):
            dp[i] = min(dp[i],dp[i-j**2]+1)

    print(dp[num])