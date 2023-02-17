import sys
import bisect
import copy

length = int(sys.stdin.readline().rstrip())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
num_list_rev = num_list[::-1]
dp = [0 for _ in range(length)]
dp_rev = [0 for _ in range(length)]

dp[0] = 1
dp_rev[0] = 1

for i in range(1,length):
    for j in range(i):
        if num_list[i] < num_list[j]:
            dp[i] = max(dp[i],dp[j]+1)
        else:
            dp[i] = max(dp[i],1)

print(max(dp))