import sys
from collections import deque

size = int(sys.stdin.readline().rstrip())
q = deque(enumerate(map(int, sys.stdin.readline().rstrip().split())))

result = []
while q:
    idx, p = q.popleft()
    result.append(idx + 1)

    if p > 0:
        q.rotate(-(p - 1))
    else:
        q.rotate(-p)

print(" ".join(map(str, result)))
