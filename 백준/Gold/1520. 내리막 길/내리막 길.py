import sys

row,col = map(int,sys.stdin.readline().rstrip().split())
board = [] 
delta = [(1,0),(-1,0),(0,1),(0,-1)]

dp = [ [-1 for _ in range(col)] for _ in range(row)]
# dp의 초깃값을 -1로 설정한다. 들리지 않은 경우를 -1로 하기 위함
# -1로 설정하는 것이 굉장히 중요하다!
# 왜냐하면 0으로 설정하면 들렸는데 경로의 수가 0인 건지
# 아니면 안들린건지 판별이 불가능하기 때문에
# 들렸는데 경로의 수가 0인 경우에도 계속 방문을 하게 됨
# 하지만 -1로 초기화 후에 들렸는데 경로가 0인 경우에는
# dp 값이 0 이기 때문에 들렸다는 것을 확인이 가능하다

for _ in range(row):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

def dfs(y,x):
    if y == row -1  and x == col - 1:
        return 1
        # 도착 지점에 도달한 경우 경로의 수를 1 추가
    
    # 이미 들렀던 경우에는
    # (y,x) 에서(row,col) 까지 가는 경로의 수인
    # dp[y][x]를 호출 하고 DFS 종료
    if dp[y][x] != -1:
        return dp[y][x]
    
    
    dp[y][x] = 0
    # 0으로 바꿔서 들렸다고 표시하고 row,col 까지 가는 경로의 수를 0으로 초기화
    for dy,dx in delta:
        ny,nx = y+dy,x+dx

        if  ny == -1 or ny == row or nx == -1 or nx == col :
            continue
        if board[y][x] <= board[ny][nx]:
            continue
        dp[y][x] += dfs(ny,nx)

    return dp[y][x]

print(dfs(0,0))