import sys

f = sys.stdin
# f = open("practice.txt","r")

size = int(f.readline().rstrip())
table = [list(map(int,f.readline().rstrip().split())) for _ in range(size)]

dp = [2000000] * (1<<size)
dp[0] = 0

# 1의 개수 측정 
def bit_count(x):
    cnt = 0
    while x:
        cnt += x&1
        x >>= 1
    
    return cnt

for i in range(1<<size):
    k = bit_count(i)
    for j in range(size):
        if i & (1<<j):
            continue
        dp[i|1<<j] = min(dp[i|1<<j], dp[i]+table[k][j])
    
print(dp[-1])