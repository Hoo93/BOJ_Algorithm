import sys
from collections import deque
width,height = map(int,sys.stdin.readline().rstrip().split())

square = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(height) ]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

tomato_list = []
# Tomato 가 있는 좌표 추출
for i in range(height):
    for j in range(width):
        if square[i][j] == 1:
            tomato_list.append([i,j,1])
            square[i][j] = 0

que = deque(tomato_list)

mx = -1
while que:
    y,x,distance = que.popleft()

    if x<0 or x>=width or y<0 or y>=height or square[y][x] != 0:
        continue

    square[y][x] = distance
    mx = max(mx,distance)
    for i,j in zip(dx,dy):
        que.append((y+j,x+i,distance+1))
    
imposible = False
for i in range(height):
    for j in range(width):
        if square[i][j] == 0:
            imposible = True
            break
    if imposible:
        break

if not imposible:
    print(mx-1)
else:
    print(-1)