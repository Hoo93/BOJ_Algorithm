import sys
import math

num = int(sys.stdin.readline().rstrip())
if num % 2 == 1:
    print(0)
else:
    dp = [1,3,11] + [0 for _ in range(num-2)]
    num //= 2
    if num <= 2:
        print(dp[num])
    else:
        for i in range(3,num+1):
            cnt = i-2
            dp[i] = dp[i-1]*3
            while cnt >=0:
                dp[i] += 2*dp[cnt]
                cnt -= 1
        print(dp[num])