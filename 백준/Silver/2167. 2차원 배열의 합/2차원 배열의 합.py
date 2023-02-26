import sys

row,col = map(int,sys.stdin.readline().rstrip().split())
board = [[0 for _ in range(col+1)]]+[[0]+list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(row)]
case_num = int(sys.stdin.readline().rstrip())
cases = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(case_num)]

for i in range(1,row+1):
    for j in range(1,col+1):
        board[i][j] += board[i][j-1]

for case in cases:
    y1,x1,y2,x2 = case
    result = 0 
    for i in range(y1,y2+1):
        result += board[i][x2] - board[i][x1-1]
    print(result)