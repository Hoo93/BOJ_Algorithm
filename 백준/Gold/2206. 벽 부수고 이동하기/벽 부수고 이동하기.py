import sys
from collections import deque

row,col = map(int,sys.stdin.readline().rstrip().split())
board = ["-"*(col+2)] + ["-"+sys.stdin.readline().rstrip()+"-" for _ in range(row)] + ["-"*(col+2)]
visited = [[[0,0] for _ in range(col+2)] for _ in range(row+2)]
delta = [(1,0),(-1,0),(0,1),(0,-1)]

visited[1][1][0] = 1

que = deque([(1,1,0)])

while que:
    y,x,wall = que.popleft()
    
    for dy,dx in delta:
        ny,nx,nwall = y+dy,x+dx,wall
        if board[ny][nx] == "-":
            continue
        elif board[ny][nx] == "1":
            nwall += 1
        if nwall > 1:
            continue
        if  0 < visited[ny][nx][nwall]:
            continue

        que.append((ny,nx,nwall))
        visited[ny][nx][nwall] = visited[y][x][wall] + 1

if 0 in visited[row][col]:
    answer = max(visited[row][col])
else:
    answer = min(visited[row][col])
print(answer if answer != 0 else -1 )