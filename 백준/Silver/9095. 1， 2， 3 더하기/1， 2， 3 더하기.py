import sys
import bisect

num = int(sys.stdin.readline())
nums = []
for _ in range(num):
    nums.append(int(sys.stdin.readline().rstrip()))

mx = max(nums)

dp = [0 for _ in range(mx+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,mx+1):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for i in nums:
    print(dp[i])