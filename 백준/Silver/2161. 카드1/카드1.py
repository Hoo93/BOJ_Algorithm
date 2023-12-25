import sys
from collections import deque

size = int(sys.stdin.readline().rstrip())
q = deque([num for num in range(2, size + 1)])
result = "1"

while len(q):
    q.append(q.popleft())
    result += " " + str(q.popleft())

print(result)
