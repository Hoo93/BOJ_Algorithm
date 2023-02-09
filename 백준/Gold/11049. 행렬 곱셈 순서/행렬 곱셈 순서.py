import sys
from collections import deque

mat_num = int(sys.stdin.readline().rstrip())
mats = [ 0 for _ in range(mat_num+1)]
dp = [ [0 for _ in range(mat_num+1)] for _ in range(mat_num+1)]

for i in range(mat_num):
    mats[i+1] = list(map(int,sys.stdin.readline().rstrip().split()))
    dp[i+1][i+1] = 0

for i in range(1,mat_num):
    dp[i][i+1] = mats[i][0]*mats[i][1]*mats[i+1][1]

for i in range(mat_num-2,0,-1):
    for j in range(i+2,mat_num+1):
        mn = 2**31
        for k in range(i,j):
            mn = min(mn,dp[i][k]+dp[k+1][j]+mats[i][0]*mats[k][1]*mats[j][1])
        dp[i][j] = mn
        
print(dp[1][mat_num])