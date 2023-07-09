import sys

f = sys.stdin
# f = open("input.txt","r")

dp = [1 for _ in range(21)]

for i in range(1,21):
    dp[i] = dp[i-1]*i

N = int(f.readline().rstrip())

print(dp[N])