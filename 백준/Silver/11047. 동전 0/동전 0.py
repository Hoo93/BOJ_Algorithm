import sys
import bisect
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))

idx = bisect.bisect_right(coins,k) - 1
result = 0

while k > 0:
    result += k//coins[idx]
    k %= coins[idx]
    idx -= 1

print(result)    