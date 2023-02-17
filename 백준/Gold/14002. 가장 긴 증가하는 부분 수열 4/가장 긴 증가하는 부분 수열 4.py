import sys
import bisect
import copy

length = int(sys.stdin.readline().rstrip())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [[] for _ in range(length)]

for i in range(length):
    dp[i].append(num_list[i])

for i in range(1,length):
    for j in range(i):
        if num_list[j] < num_list[i]:
            if len(dp[j])+1 > len(dp[i]):
                dp[i] = dp[j] + [num_list[i]]
idx = 0
mx = 0
for i in range(length):
    if mx < len(dp[i]):
        idx = i
        mx = len(dp[i])

print(mx)
print(" ".join(map(str,dp[idx])))