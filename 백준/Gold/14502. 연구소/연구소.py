import sys
import copy
import itertools
sys.setrecursionlimit(10**6)

row,col = map(int,sys.stdin.readline().rstrip().split())
board = [[ 1 for _ in range(col+2)]] +[ [1] + list(map(int,sys.stdin.readline().rstrip().split()))+[1] for _ in range(row)] +[ [1 for _ in range(col+2)]] 
virus = []
points = []
delta = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(1,row+1):
    for j in range(1,col+1):
        points.append((i,j))

walls = list(itertools.combinations(points,3))

for i in range(1,row+1):
    for j in range(1,col+1):
        if board[i][j] == 2:
            virus.append((i,j))

def dfs(nboard,y,x):
    for dy,dx in delta:
        ny = y + dy
        nx = x + dx
        if nboard[ny][nx] == 0:
            nboard[ny][nx] = 2
            dfs(nboard,ny,nx)

def make_wall(wall):
    for y,x in wall:
        if board[y][x] != 0:
            return 0
    
    nboard = copy.deepcopy(board)
    for y,x in wall:
        nboard[y][x] = 1
    
    for y,x in virus:
        dfs(nboard,y,x)

    cnt = 0
    for i in range(1,row+1):
        for j in range(1,col+1):
            if nboard[i][j] == 0:
                cnt += 1
    return cnt
                

result = 0 
for wall in walls:
    result = max(make_wall(wall),result)

print(result)