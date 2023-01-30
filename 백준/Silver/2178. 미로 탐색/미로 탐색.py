import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)

height,width = map(int,sys.stdin.readline().rstrip().split())

square = ["0"*(width+2)] + ["0" + sys.stdin.readline().rstrip() +"0" for _ in range(height)] + ["0"*(width+2)]

visited = [[0 for _ in range(width+2)] for _ in range(height+2)]

que = deque()
que.append((1,1,1))
while que:
    y,x,distance = que.popleft()
    if visited[y][x] > 0:
        continue
    visited[y][x] = distance

    if square[y+1][x] == "1": que.append((y+1,x,distance+1))
    if square[y-1][x] == "1": que.append((y-1,x,distance+1))
    if square[y][x+1] == "1": que.append((y,x+1,distance+1))
    if square[y][x-1] == "1": que.append((y,x-1,distance+1))

print(visited[height][width])