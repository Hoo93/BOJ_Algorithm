import sys

row,col = map(int,sys.stdin.readline().rstrip().split())
board = [] 
delta = [(1,0),(-1,0),(0,1),(0,-1)]
dp = [ [-1 for _ in range(col)] for _ in range(row)]

for _ in range(row):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

def dfs(y,x):
    if y == row -1  and x == col - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for dy,dx in delta:
        ny,nx = y+dy,x+dx

        if  0 <= ny < row and 0 <= nx < col :
            if board[y][x] > board[ny][nx]:
                dp[y][x] += dfs(ny,nx)

    return dp[y][x]
print(dfs(0,0))