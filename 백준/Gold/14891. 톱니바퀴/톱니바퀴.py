import sys
from collections import deque

def rotate_gear(idx,dir):
    idx -= 1
    dirs = [0 for _ in range(4)]
    que = deque()
    que.append((idx,dir))
    
    while que:
        idx,dir = que.popleft()
        if dirs[idx] != 0:
            continue
        dirs[idx] = dir
        
        for i in [1,-1]:
            nidx = idx + i
            if nidx < 0 or nidx > 3:
                continue
            if gears[idx][4-2*i] == gears[nidx][4+2*i]:
                dirs[nidx]=0
            else:
                que.append((nidx,-1*dir))
            
    for i in range(len(gears)):
        gears[i] = (gears[i]*3)[8-dirs[i]:16-dirs[i]]
    
gears = [sys.stdin.readline().rstrip() for _ in range(4)]
orders = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline().rstrip()))]

for idx,dir in orders:
    rotate_gear(idx,dir)

result = 0
for i in range(4):
    result += 2**i*int(gears[i][0])

print(result)