import sys
import math

input = sys.stdin.readline
n,k = map(int,input().rstrip().split())

def mul_DAC(a,b):
    if b == 1:
        return a
    else:
        if b%2 == 0:
            return mul_DAC(a,b//2)**2%1000000007
        else:
            return mul_DAC(a,(b-1)//2)**2*a%1000000007

dp = [1,1] + [0 for _ in range(n-1)]

for i in range(2,n+1):
    dp[i] = dp[i-1]*i%1000000007

print(dp[n]*mul_DAC(dp[k]*dp[n-k],1000000005)%1000000007)
