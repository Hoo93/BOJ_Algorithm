import sys
input = sys.stdin.readline

row,col,size = map(int,input().rstrip().split())
bw = ["BW"*col, "WB"*col]
board = [input().rstrip() for _ in range(row)]
prefix_board = [[0 for _ in range(col+1)] for _ in range(row+1)]

# prefix_sum == i행 j열 까지 (0,0) 성분이 B인 체스판과 비교했을 때 올바르게 칠해진 타일의 개수 구하기
for i in range(row):
    idx = i%2
    for j in range(col):
        if board[i][j] == bw[idx][j]:
            prefix_board[i+1][j+1] = prefix_board[i+1][j] + 1
        else:
            prefix_board[i+1][j+1] = prefix_board[i+1][j]

    for j in range(col):
        prefix_board[i+1][j+1] += prefix_board[i][j+1]

# prefix_sum을 이용해 (x,y) 에서 (x+size-1,y+size-1) 까지 다시 칠해야하는 체스판의 개수 구하기
def get_recolor(x:int,y:int):
    result = prefix_board[y+size][x+size] - prefix_board[y+size][x] - prefix_board[y][x+size] + prefix_board[y][x]
    return min(result,size**2 - result)

# (i,j)를 시작점으로 하여 다시 칠해야하는 체스판의 개수의 최솟값 구하기
answer = row*col
for i in range(row-size+1):
    for j in range(col-size+1):
        tmp  = get_recolor(j,i)
        if tmp < answer:
            answer = tmp

print(answer)
