import sys

n,k = map(int,input().strip().split())
answer = 1
for i in range(k):
    answer *= (n-i)

for i in range(1,k+1):
    answer //= i

print(answer)