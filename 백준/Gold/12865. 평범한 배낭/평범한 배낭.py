import sys

input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
stuff = [(0,0)]+[tuple(map(int,input().rstrip().rsplit())) for _ in range(n) ]

dp = [0 for _ in range(k+1)]

for i in range(1,n+1):
    weight = stuff[i][0]
    value  = stuff[i][1]
    for j in range(k,0,-1):
        

        if weight > j:
            break
        else:
            dp[j] = max(dp[j],dp[j-weight]+value)

print(dp[k])