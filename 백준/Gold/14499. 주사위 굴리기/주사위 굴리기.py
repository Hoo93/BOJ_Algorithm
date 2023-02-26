import sys

# 동쪽 U D N S E W --> W E N S U D
# 서쪽 U D N S E W --> E W N S D U
# 북쪽 U D N S E W --> S N U D E W
# 남쪽 U D N S E W --> N S D U E W



def move_dice(order):
    global r,c
    if order == 1:
        c += 1
        if r < 0 or r > row-1 or c < 0 or c > col-1:
            c -= 1
            return -1
        dice[0],dice[1],dice[4],dice[5] = dice[5],dice[4],dice[0],dice[1]
        if board[r][c] == 0:
            board[r][c] = dice[1]
        else:
            dice[1],board[r][c] = board[r][c],0
        return dice[0]
    if order == 2:
        c -= 1
        if r < 0 or r > row-1 or c < 0 or c > col-1:
            c += 1
            return -1
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[5],dice[1],dice[0]
        if board[r][c] == 0:
            board[r][c] = dice[1]
        else:
            dice[1],board[r][c] = board[r][c],0
        return dice[0]
    if order == 3:
        r -= 1
        if r < 0 or r > row-1 or c < 0 or c > col-1:
            r += 1
            return -1
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[2],dice[0],dice[1]
        if board[r][c] == 0:
            board[r][c] = dice[1]
        else:
            dice[1],board[r][c] = board[r][c],0
        return dice[0]
    if order == 4:
        r += 1
        if r < 0 or r > row-1 or c < 0 or c > col-1:
            r -= 1
            return -1
        dice[0],dice[1],dice[2],dice[3] = dice[2],dice[3],dice[1],dice[0]
        if board[r][c] == 0:
            board[r][c] = dice[1]
        else:
            dice[1],board[r][c] = board[r][c],0
        return dice[0]

row,col,r,c,order_num = map(int,sys.stdin.readline().rstrip().split())
board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(row)]
orders = list(map(int,sys.stdin.readline().rstrip().split()))
# E:1 / W:2 / N:3 / S:4

# U D N S E W
dice = [0,0,0,0,0,0]
for order in orders:
    tmp = move_dice(order)
    if tmp == -1:
        continue
    else:
        print(tmp)