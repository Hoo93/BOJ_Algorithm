import sys
import heapq

length = int(sys.stdin.readline().rstrip())

dp =[[1 for _ in range(length+1)]] +[ [ 0 for _ in range(length+1)] for _ in range(9)]

for i in range(1,10):
    dp[i][1] = 1

for i in range(2,length+1):
    sumation = 1
    for j in range(1,10):
        sumation += dp[j][i-1]
        dp[j][i] = sumation%10007

result = 0
for i in range(10):
    result += dp[i][length]

print(result%10007)