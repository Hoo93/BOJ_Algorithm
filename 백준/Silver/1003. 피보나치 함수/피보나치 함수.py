import sys
input = sys.stdin.readline

n = int(input().strip())
nlt = []
for i in range(n):
    nlt.append(int(input().strip()))

dp = [[1,0],[0,1],[1,1],[1,2]] + [[0,0] for _ in range(38)]

for i in range(4,max(nlt)+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for num in nlt:
    print(dp[num][0],dp[num][1])
