import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
test_num = int(sys.stdin.readline())
for _ in range(test_num):
    width,height,num = map(int,sys.stdin.readline().rstrip().split())
    
    square = [ [0 for _ in range(width+2)] for _ in range(height+2) ]
    visited = [[False for _ in range(width+2)] for _ in range(height+2) ]
    que = deque()
    count = 0
    
    for _ in range(num):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        square[y+1][x+1] = 1
    
    for i in range(1,height+1):
        for j in range(1,width+1):
            if square[i][j] and not visited[i][j]:
                count += 1
                que.append((i,j))
    
                while que:
                    y,x = que.popleft()
                    if visited[y][x]:
                        continue
                    visited[y][x] = True
                    if square[y+1][x]: que.append((y+1,x))
                    if square[y-1][x]: que.append((y-1,x))
                    if square[y][x+1]: que.append((y,x+1))
                    if square[y][x-1]: que.append((y,x-1))
                
    print(count)