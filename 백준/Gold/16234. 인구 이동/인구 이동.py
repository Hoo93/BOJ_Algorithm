import sys
from collections import deque

delta = [(1,0),(-1,0),(0,1),(0,-1)]

    
def check():
    visited = [[0 for _ in range(size)] for _ in range(size)]
    flag = False

    def bfs(r,c):
        que = deque()
        que.append((r,c))
        result = 0
        points_set = set()
        
        while que:
            y,x = que.popleft()
            if visited[y][x] > 0:
                continue
            visited[y][x] = 1
            result += board[y][x]
            points_set.add((y,x))
            for dy,dx in delta:
                ny,nx = y+dy,x+dx
                if ny < 0 or ny > size-1 or nx < 0 or nx > size-1:
                    continue
                if visited[ny][nx] > 0:
                    continue
                if L <= abs(board[y][x]-board[ny][nx]) <= R:
                    que.append((ny,nx))
        if len(points_set) != 0:
            result //= len(points_set)
            for y,x in points_set:
                board[y][x] = result
    
    for i in range(size):
        for j in range(size-1):
            if visited[i][j] > 0: continue
            if L <= abs(board[i][j]-board[i][j+1]) <= R:
                flag = True
                bfs(i,j)
    for j in range(size):
        for i in range(size-1):
            if visited[i][j] > 0: continue
            if L <= abs(board[i+1][j]-board[i][j]) <= R:
                flag = True
                bfs(i,j)

    return flag



size,L,R = map(int,sys.stdin.readline().rstrip().split())
board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(size)]

cnt = 0
flag = check()
while flag:
    cnt +=1
    flag = check()

print(cnt)