import sys
import bisect
import copy

length = int(sys.stdin.readline().rstrip())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(length)]

dp[0] = num_list[0]

for i in range(1,length):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i],dp[j]+num_list[i])
        else:
            dp[i] = max(dp[i],num_list[i])

print(max(dp))