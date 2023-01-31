import sys
from collections import deque
col,row,height = map(int,sys.stdin.readline().rstrip().split())
wall = [ [-1 for _ in range(col+2)] for _ in range(row+2) ]

tomato_list = []
tomato_list.append(wall)
for _ in range(height):
    tmp = [[-1 for _ in range(col+2) ]] + [ [-1] + list(map(int,sys.stdin.readline().rstrip().split())) + [-1] for _ in range(row)] + [[-1 for _ in range(col+2) ] ]
    tomato_list.append(tmp)
tomato_list.append(wall)

cnt = 0
start_point = []
mx = 0

delta = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

for i in range(1,height+1):
    for j in range(1,row+1):
        for k in range(1,col+1):
            if tomato_list[i][j][k] == 1:
                start_point.append((i,j,k,1))
                tomato_list[i][j][k] = 0
                cnt += 1
            elif tomato_list[i][j][k] == 0:
                cnt += 1

que = deque(start_point)
while que:
    z,y,x,distance = que.popleft()
    if tomato_list[z][y][x] != 0:
        continue
    tomato_list[z][y][x] = distance
    cnt -= 1
    mx = max(mx,distance)
    for dz,dy,dx in delta:
        nz,ny,nx = z+dz,y+dy,x+dx
        que.append((nz,ny,nx,distance+1))

print(mx-1 if cnt == 0 else -1)

