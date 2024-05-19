import sys
import math
from collections import deque

#file = open('prac.txt','r')
#input = file.readline

input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]
K = int(input())
R = [[(j*10**len(str(S[i]))+S[i])%K for j in range(K)] for i in range(N)]

dp = [ [0 for _ in range(K)] for _ in range(1<<N)]
dp[0][0] = 1

for i in range(1<<N):
    for j in range(N):
        if i & 1<<j: continue
        for k in range(K):
            dp[i|1<<j][R[j][k]] += dp[i][k]


if dp[-1][0] == 0:
    print('0/1')
else:
    sm = sum(dp[-1])
    gcd = math.gcd(sm,dp[-1][0])
    print("{}/{}".format(dp[-1][0]//gcd,sm//gcd))
