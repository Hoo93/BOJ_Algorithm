import sys
from collections import deque
import copy

sys.setrecursionlimit(10**7)

def supervise(board,y,x,dir):
    # 북쪽
    if dir == 0:
        for r in range(y-1,-1,-1):
            if board[r][x] == 6:
                break
            board[r][x] = 1
    
    if dir == 1:
        for c in range(x+1,col):
            if board[y][c] == 6:
                break
            board[y][c] = 1
    
    if dir == 2:
        for r in range(y+1,row):
            if board[r][x] == 6:
                break
            board[r][x] = 1

    if dir == 3:
        for c in range(x-1,-1,-1):
            if board[y][c] == 6:
                break
            board[y][c] = 1
    
    return board

def camera(board,point,dir):
    type,y,x = point
    if type == 1:
        return supervise(board,y,x,dir)
    
    if type == 2:
        dir %= 2
        board = supervise(board,y,x,dir)
        board = supervise(board,y,x,dir+2)
        return board
    
    if type == 3:
        board = supervise(board,y,x,dir)
        board = supervise(board,y,x,(dir+1)%4)
        return board
    
    if type == 4:
        board = supervise(board,y,x,dir)
        board = supervise(board,y,x,(dir+1)%4)
        board = supervise(board,y,x,(dir+2)%4)
        return board
    
    if type == 5:
        board = supervise(board,y,x,0)
        board = supervise(board,y,x,1)
        board = supervise(board,y,x,2)
        board = supervise(board,y,x,3)
        return board

def dfs(board,cnt):
    global mn
    if cnt == len(points):
        cnt = 0 
        for r in range(row):
            for c in range(col):
                if board[r][c] == 0:
                    cnt += 1
        mn = min(mn,cnt)
    else:
        for i in range(4):
            nboard = copy.deepcopy(board)
            dfs(camera(nboard,points[cnt],i),cnt+1)

row,col = map(int,sys.stdin.readline().rstrip().split())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(row)]
mn = row*col

points = []
for r in range(row):
    for c in range(col):
        if board[r][c] == 0 or board[r][c] == 6:
            continue
        points.append((board[r][c],r,c))

dfs(board,0)
print(mn)