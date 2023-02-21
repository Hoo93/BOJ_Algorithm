import sys
from collections import deque
import heapq
size = int(sys.stdin.readline().rstrip())
board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(size)]
fishes = [ [False for _ in range(size)] for _ in range(size)]
shark_y,shark_x = 0,0
shark_size,feed,time,dist = 2,0,0,0

delta = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(size):
    for j in range(size):
        if board[i][j] > 0:
            if board[i][j] == 9:
                shark_y,shark_x = i,j
            else:
                fishes[i][j] = True

def bfs(row,col,volume)->tuple:
    que = deque()
    result = []
    que.append((0,row,col))
    dist_board = [ [-1 for _ in range(size)] for _ in range(size)]
    dist_board[row][col] = 0
    while que:
        dist,y,x = que.popleft()
        
        for dy,dx in delta:
            ny,nx = y+dy,x+dx
            if 0 <= ny < size and 0 <= nx < size:
                if dist_board[ny][nx] >= 0:
                    continue
                if board[ny][nx] > volume:
                    continue
                if fishes[ny][nx] and board[ny][nx] < volume:
                    result.append((dist+1,ny,nx))
                dist_board[ny][nx] = dist+1
                que.append((dist+1,ny,nx))

        if not que:
            break

        if len(result) > 0:
            if result[0][0] < que[0][0]:
                break
    
    
    if len(result) == 0:
        return (-1,0,0)

    mn = (size**2,size,size)
    for d,r,c in result:
        if d < mn[0]:
            mn = (d,r,c)
        elif d == mn[0]:
            if r < mn[1]:
                mn = (d,r,c)
            elif r == mn[1]:
                if c < mn[2]:
                    mn = (d,r,c)
    return mn

if len(fishes[1]) == 0:
    print(0)
else:
    while True:
        board[shark_y][shark_x] = 0
        dist,shark_y,shark_x = bfs(shark_y,shark_x,shark_size)
        if dist == -1:
            break
        time += dist
        fishes[shark_y][shark_x] = False
        board[shark_y][shark_x] = 0
        feed += 1
        if feed == shark_size:
            feed = 0
            shark_size += 1

    print(time)