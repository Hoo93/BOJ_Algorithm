import sys

input = sys.stdin.readline
num = int(input().rstrip())
num_list =list(map(int,input().rstrip().split()))

dp = [0 for _ in range(num)]
dp[0] = 1
idx,maximum = 0,num_list[0]
for i in range(1,num):
    for j in range(i):
        if num_list[i] > num_list[j] and dp[i] < dp[j]:
            dp[i]= dp[j]
    dp[i] += 1

print(max(dp))
    