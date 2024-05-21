import sys
import math
from collections import deque

# file = open('prac.txt','r')
# input = file.readline

input = sys.stdin.readline

N = int(input())
K = int(input())

dp = [[[-1 for _ in range(2)] for _ in range(K+1)] for _ in range(N+1)]

dp[0][0][0] = 1
dp[0][0][1] = 0
dp[0][1][0] = 0
dp[0][1][1] = 0

for i in range(1,N+1):
    dp[i][1][1] = 1
    dp[i][0][1] = 0
    dp[i][0][0] = 1
    dp[i][1][0] = i-1


# 이게 잘못됨
# 수정 : 4 2 1 =  2 1 0 + 
# 수정 : 4 2 0 =  2 1 0 + 3 2 0
# N X 1 = (N-1) X 1 + (N-2)(X-1)1
# N X 0 = (N-2)(X-1)0 + (N-1) X 0

def dfs(x,y,z):
    if y > x //2:
        return 0
    
    if y == 0 | y == 1:
        return dp[x][y][z]
    
    if dp[x][y][z] > -1:
        return dp[x][y][z]
    
    result = 0
    if z == 1:
        result = dfs(x-2,y-1,0)
        dp[x][y][z] = result
        return result
    else:
        result = dfs(x-2,y-1,0) + dfs(x-1,y,0)
        dp[x][y][z] = result
        return result

result = dfs(N,K,0) + dfs(N,K,1)
print(result%1_000_000_003)
