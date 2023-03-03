import sys
from collections import deque
import copy

sys.setrecursionlimit(10**7)

def melt(que):
    tmp = deque()

    while que:
        y,x,h = que.popleft()

        for dy,dx in delta:
            ny,nx = y+dy,x+dx
            if icebergs[ny][nx] == 0:
                if h == 0:
                    break
                h -= 1
        
        tmp.append((y,x,h))

    for y,x,h in tmp:
        icebergs[y][x] = h
        if h == 0:
            continue
        que.append((y,x,h))
    return que

def bfs(que):
    # TO DO
    # visited dict ? 로 정리
    
    visited = dict()
    length = len(que)
    if length == 0:
        return False
    n_que = deque()
    n_que.append(que[0])
    while n_que:
        y,x,h = n_que.popleft()
    
        if visited.get((y,x),0) == 1:
            continue
        
        visited[(y,x)] = 1
        
        for dy,dx in delta:
            ny,nx = y+dy,x+dx
            if icebergs[ny][nx] <= 0:
                continue
            if visited.get((ny,nx),0) == 1:
                continue
            n_que.append((ny,nx,h))
        
    if sum(visited.values()) == length:
        return True
    else:
        return False

delta = [(1,0),(-1,0),(0,-1),(0,1)]
row,col = map(int,sys.stdin.readline().rstrip().split())
icebergs = [[-1 for _ in range(col+2)]] + [[-1] + list(map(int,sys.stdin.readline().rstrip().split())) + [-1] for _ in range(row)] + [[-1 for _ in range(col+2)]]

que = deque()
for r in range(1,row+1):
    for c in range(1,col+1):
        if icebergs[r][c] == 0:
            continue
        que.append((r,c,icebergs[r][c]))

result = 0
flag = bfs(que)
while flag:
    result += 1
    que = melt(que)
    if len(que) == 0: result = 0
    flag = bfs(que)

print(result)