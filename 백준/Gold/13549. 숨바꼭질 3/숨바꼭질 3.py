import sys
from collections import deque

INF = 10**6

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# nums = f.readlines()
start, destination = map(int, sys.stdin.readline().rstrip().split())

dp = [INF for _ in range(100001)]

que = deque()
que.append((start, 0))

while que:
    loc, time = que.popleft()
    if time >= dp[loc]:
        continue
    dp[loc] = time

    if loc - 1 >= 0:
        que.append((loc - 1, time + 1))
    if loc + 1 <= 100000:
        que.append((loc + 1, time + 1))
    if 2 * loc <= 100000:
        que.append((2 * loc, time))

print(dp[destination])
