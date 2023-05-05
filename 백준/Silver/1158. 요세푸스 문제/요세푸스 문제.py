import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
queue = deque([i for i in range(1, N + 1)])
result = []

while len(result) < N:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")
