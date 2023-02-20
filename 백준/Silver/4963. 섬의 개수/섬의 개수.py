import sys
import bisect
sys.setrecursionlimit(10**7)
delta = [(-1,0),(0,1),(1,0),(0,-1),(-1,1),(-1,-1),(1,1),(1,-1)]

def dfs(y,x):
    visited[y][x] = True

    for dy,dx in delta:
        ny,nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w:
            if visited[ny][nx]:
                continue
            if board[ny][nx] == 0:
                continue
            dfs(ny,nx)

while True:
    w,h = map(int,sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]
    visited = [ [False for _ in range(w)] for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    
    print(cnt)