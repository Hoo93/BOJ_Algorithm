import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)

x1,x2 = map(int,sys.stdin.readline().rstrip().split())
length = 100001
line = [0 for _ in range(100001)]

que = deque()
que.append((x1,0))

if x1 == x2:
    print(0)
else:
    while line[x2] == 0:
        point,distance = que.popleft()
        if line[point] > 0:
            continue
        line[point] = distance
        if point+1 < 100001: que.append((point+1,distance+1))
        if point-1 >= 0: que.append((point-1,distance+1))
        if point*2 < 100001: que.append((point*2,distance+1))
    
    print(line[x2])