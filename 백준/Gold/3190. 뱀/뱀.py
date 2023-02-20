import sys
from collections import deque

size = int(sys.stdin.readline().rstrip())
direction = [(0,1),(1,0),(0,-1),(-1,0)]
snake = [[False for _ in range(size)] for _ in range(size)]
apple = [[False for _ in range(size)] for _ in range(size)]
E,S,W,N = 0,1,2,3

for _ in range(int(sys.stdin.readline().rstrip())):
    y,x = map(int,sys.stdin.readline().rstrip().split())
    apple[y-1][x-1] = True

dir_list = [ 0 for _ in range(10001)]
for i in range(int(sys.stdin.readline().rstrip())):
    t,d = sys.stdin.readline().rstrip().split()
    if d == "D": dir_list[int(t)] = 1
    else: dir_list[int(t)] = -1

que = deque()
que.append((0,0,0))
result = 0
for i in range(1,10001):
    result = i
    y,x,d = que[-1]
    ny,nx = y+direction[d][0],x+direction[d][1]
    if ny < 0 or ny >= size or nx < 0 or nx >= size:
        break
    if snake[ny][nx]:
        break
    snake[ny][nx] = True
    if not apple[ny][nx]:
        tmp = que.popleft()
        snake[tmp[0]][tmp[1]] = False
    else:
        apple[ny][nx] = False
    
    que.append((ny,nx,(d+4+dir_list[i])%4))

print(result)