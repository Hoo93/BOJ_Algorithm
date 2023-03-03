import sys
from collections import deque
import copy

sys.setrecursionlimit(10**7)

delta = [(1,0),(-1,0),(0,-1),(0,1)]
row,col = map(int,sys.stdin.readline().rstrip().split())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(row)]
result = 0
cnt = 0
for r in range(row): result += sum(board[r])

def bfs():
    result = 0
    visited = [[False for _ in range(col)] for _ in range(row)]
    que = deque()
    que.append((0,0))

    while que:
        y,x = que.popleft()
        if visited[y][x]: continue
        visited[y][x] = True

        for dy,dx in delta:
            ny,nx = y+dy,x+dx
            if ny < 0 or ny > row-1: continue 
            if nx < 0 or nx > col-1: continue
            if board[ny][nx] == 1:
                board[ny][nx] = 0
                visited[ny][nx] = True
            else:
                if visited[ny][nx]: continue
                que.append((ny,nx))
    
    for r in range(row):
        result += sum(board[r])
    return result


while True:
    cnt += 1
    tmp = bfs()
    if tmp > 0:
        result = tmp
    else: break

print(cnt)
print(result)