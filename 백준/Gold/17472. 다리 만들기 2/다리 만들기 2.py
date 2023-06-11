import sys
from collections import deque

# f = open("practice.txt","r")
# row,col = map(int,f.readline().rstrip().split())
# board = [ list(map(int,f.readline().rstrip().split())) for _ in range(row) ]


def bfs(r,c,flag):
    queue = deque()
    queue.append((r,c))

    while queue:
        y,x = queue.popleft()
        
        if board[y][x] == flag:
            continue
        
        board[y][x] = flag

        for dy,dx in delta:
            ny,nx = y+dy, x+dx

            if 0 <= ny < row and 0 <= nx < col and board[ny][nx]:
                queue.append((ny,nx))

def findBrdige(r,c,flag):
    queue = deque()
    queue.append((r,c))

    while queue:
        y,x = queue.popleft()
        
        if board[y][x] != flag or visited[y][x]:
            continue
        
        visited[y][x] = True
        board[y][x] = flag

        for dy,dx in delta:
            ny,nx = y+dy, x+dx
            if ny < 0 or ny >= row or nx < 0 or nx >= col:
                continue
            if board[ny][nx] == 0:
                length = 0

                while True:
                    ny += dy
                    nx += dx
                    if ny < 0 or ny >= row or nx < 0 or nx >= col:
                        break
                    elif board[ny][nx] == flag:
                        break
                    elif board[ny][nx] != 0 and board[ny][nx] != flag:
                        bridges.append((length+1,flag,board[ny][nx]))
                        break
                    else:
                        length += 1

            elif board[ny][nx] == flag:
                queue.append((ny,nx))

def find(node):
    if roots[node] == node:
        return node
    
    root = find(roots[node])
    roots[node] = root
    return roots[node]

def union(n1,n2):
    n1,n2 = find(n1),find(n2)

    if n1 == n2:
        return
    elif n1 < n2:
        roots[n2] = n1
    else:
        roots[n1] = n2

row,col = map(int,sys.stdin.readline().rstrip().split())
board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(row) ]

visited= [ [ False for _ in range(col) ] for _ in range(row) ]
delta = ((-1,0),(1,0),(0,1),(0,-1))

bridges = []
result = 0
cnt = 0

flag = 2
start_point = []
for r in range(row):
    for c in range(col):
        if board[r][c] == 1:
            start_point.append((r,c,flag))
            bfs(r,c,flag)
            flag += 1            

roots = [ i for i in range(flag)]

for r,c,flag in start_point:
    findBrdige(r,c,flag)

bridges.sort()

for length,node1,node2 in bridges:
    if length < 2:
        continue
    if find(node1) == find(node2):
        continue
    else:
        result += length
        union(node1,node2)
        cnt += 1

if len(roots) - 3 != cnt:
    result = -1
print(result)