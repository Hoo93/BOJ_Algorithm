import sys
from collections import deque
row,col = map(int,sys.stdin.readline().rstrip().split())
r,c,d = map(int,sys.stdin.readline().rstrip().split())
delta = [(-1,0),(0,1),(1,0),(0,-1),(-1,0),(0,1),(1,0),(0,-1)]
# 0 1 2 3 북 동 남 서 북 동 남 서
board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(row)] 
visited = [ [ False for _ in range(col)] for _ in range(row) ]
cnt = 0

def auto_cleaner(y,x,dir):
    global cnt
    if not visited[y][x]:
        visited[y][x] = True
        cnt += 1

    for idx in range(dir+3,dir-1,-1):
        dy,dx = delta[idx]
        ny,nx = y+dy,x+dx
        if visited[ny][nx]:
            continue
        if board[ny][nx] == 1:
            continue
        auto_cleaner(ny,nx,idx%4)
        return

    dy,dx = delta[dir]
    ny,nx = y-dy,x-dx
    
    if board[ny][nx] != 1:
        auto_cleaner(ny,nx,dir%4)
        return
    else:
        return
    
auto_cleaner(r,c,d)
print(cnt)