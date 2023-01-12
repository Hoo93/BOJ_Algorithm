import sys
from collections import deque

input = sys.stdin.readline

num = int(input().strip())

q = deque([i for i in range(1,num+1)])

for _ in range(num-1):
    q.popleft()
    q.append(q.popleft())

print(q.popleft())
