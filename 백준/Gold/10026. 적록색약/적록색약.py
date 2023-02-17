import sys
sys.setrecursionlimit(10**7)

length = int(sys.stdin.readline().rstrip())

board = [sys.stdin.readline().rstrip() for _ in range(length)]
visited = [ [False for _ in range(length)] for _ in range(length)] 
visited_rgb = [ [False for _ in range(length)] for _ in range(length)] 
delta = ((1,0),(-1,0),(0,1),(0,-1))
result = []

def dfs(char,visit,y,x):
    visit[y][x] = True
    for dy,dx in delta:
        ny,nx = y+dy,x+dx
        if 0 <= ny < length and 0 <= nx < length:
            if not visit[ny][nx] and board[ny][nx] == char:            
                dfs(char,visit,ny,nx)
        
cnt = 0
for i in range(length):
    for j in range(length):
        if not visited[i][j]:
            dfs(board[i][j],visited,i,j)
            cnt += 1
result.append(cnt)

for i in range(length):
    board[i] = board[i].replace("G","R")

cnt = 0
for i in range(length):
    for j in range(length):
        if not visited_rgb[i][j]:
            dfs(board[i][j],visited_rgb,i,j)
            cnt += 1
result.append(cnt)
print(" ".join(map(str,result)))