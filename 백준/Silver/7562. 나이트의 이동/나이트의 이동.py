import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)

test_case = int(sys.stdin.readline().rstrip())

for _ in range(test_case):
    size = int(sys.stdin.readline().rstrip())
    start_y,start_x = map(int,sys.stdin.readline().rstrip().split())
    target_y,target_x = map(int,sys.stdin.readline().rstrip().split())
    if start_x == target_x and start_y == target_y:
        print(0)
        continue
    visited = [[0 for _ in range(size)] for _ in range(size)]
    que = deque()
    que.append((start_y,start_x,0))
    
    while visited[target_y][target_x]==0:
        y,x,distance = que.popleft()
        if x<0 or y<0:
            continue
        if x>=size or y >= size:
            continue
        if visited[y][x] > 0:
            continue
        visited[y][x] = distance
        
        que.append((y+1,x+2,distance+1))
        que.append((y-1,x+2,distance+1))
        que.append((y+1,x-2,distance+1))
        que.append((y-1,x-2,distance+1))
        que.append((y+2,x+1,distance+1))
        que.append((y-2,x+1,distance+1))
        que.append((y+2,x-1,distance+1))
        que.append((y-2,x-1,distance+1))
    print(visited[target_y][target_x])