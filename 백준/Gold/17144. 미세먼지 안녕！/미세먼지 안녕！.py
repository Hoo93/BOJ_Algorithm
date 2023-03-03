import sys
from collections import deque
import copy

sys.setrecursionlimit(10**7)

delta = [(1,0),(-1,0),(0,-1),(0,1)]
row,col,time = map(int,sys.stdin.readline().rstrip().split())
board = [[-1 for _ in range(col+2)]]+[[-1]+list(map(int,sys.stdin.readline().rstrip().split()))+[-1] for _ in range(row)]+[[-1 for _ in range(col+2)]] 
cleaner = [0,0]
for r in range(1,row+1):
    if board[r][1] == -1:
        cleaner = [r,r+1]
        break

que = deque()
for r in range(1,row+1):
    for c in range(1,col+1):
        if board[r][c] > 0:
            que.append([r,c,board[r][c]])

def spread(que):
    points = set()
    while que:
        y,x,dust = que.popleft()
        points.add((y,x))
        spread_dust = dust//5
        if spread_dust == 0:
            continue
        for dy,dx in delta:
            ny,nx = y+dy,x+dx
            if board[ny][nx] <= -1:
                continue
            board[ny][nx] += spread_dust
            board[y][x] -= spread_dust
            points.add((ny,nx))
    
    for y,x in points:
        que.append((y,x,board[y][x]))
    
    return que

def clean(que):
    for _ in range(len(que)):
        y,x,dust = que.popleft()
        board[y][x] = 0
        if x == 1:
            if y == cleaner[0]-1 or y == cleaner[1]+1: continue
            else:
                if y < cleaner[0]: ny,nx = y+1,x
                else: ny,nx = y-1,x
        elif y == 1 or y == row: ny,nx = y,x-1
        elif x == col:
            if y <= cleaner[0]: ny,nx = y-1,x
            else: ny,nx = y+1,x
        elif y in cleaner: ny,nx = y,x+1
        else: ny,nx = y,x
        que.append((ny,nx,dust))
    
    for y,x,dust in que: board[y][x] = dust
    return que

for _ in range(time):
    que = spread(que)
    que = clean(que)

result =2 + 2*row
for i in board[1:row+1]: result += sum(i)
print(result)