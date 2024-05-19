import sys
from collections import deque

# file = open('prac.txt','r')
# input = file.readline

input = sys.stdin.readline

INF = 1e9

N = int(input().rstrip())

rgb = [list(map(int,input().rstrip().split())) for _ in range(N)]

result = INF

for i in range(3):
    dp = [[INF for _ in range(3)] for _ in range(N)]

    dp[0][i] = rgb[0][i]
    
    for j in range(1,N-1):
        for k in range(3):
            dp[j][k] = min(dp[j-1][(k+1)%3],dp[j-1][(k+2)%3]) + rgb[j][k]
            if dp[j][k] > INF:
                dp[j][k] = INF
    for k in range(3):
        if i == k:
            dp[-1][k] = INF
        else:
            dp[-1][k] = min(dp[N-2][(k+1)%3],dp[N-2][(k+2)%3]) + rgb[N-1][k]

    mn = min(dp[N-1])

    result = min(mn,result)

print(result)