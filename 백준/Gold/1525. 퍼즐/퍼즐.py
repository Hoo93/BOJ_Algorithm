import sys
from collections import deque
import copy

delta = [(0,1),(1,0),(0,-1),(-1,0)]
start = []
for _ in range(3):
    start += list(sys.stdin.readline().rstrip().split())

visited = dict()
idx = start.index("0")
que = deque()
que.append((start,idx,0))

while que:
    board,idx,cnt = que.popleft()
    y,x = idx//3,idx%3
    if visited.get("".join(board)) is not None:
        continue
    visited["".join(board)] = cnt

    for dy,dx in delta:
        ny,nx = y+dy,x+dx
        if ny < 0 or ny >=3 or nx < 0 or nx >=3:
            continue
        nboard = copy.deepcopy(board)
        nidx = ny*3+nx
        nboard[idx],nboard[nidx] = nboard[nidx],nboard[idx]
        que.append((nboard,nidx,cnt+1))

if visited.get("123456780") is not None:
    print(visited["123456780"])
else:
    print(-1)