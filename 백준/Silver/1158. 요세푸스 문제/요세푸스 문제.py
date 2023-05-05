import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
nlt = [i for i in range(1, N + 1)]
queue = deque([i for i in range(1, N + 1)])
result = []
for _ in range(N):
    queue.rotate(1 - K)
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")
