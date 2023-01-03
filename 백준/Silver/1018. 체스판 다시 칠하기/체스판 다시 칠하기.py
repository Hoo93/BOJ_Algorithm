import sys

row,column = map(int,sys.stdin.readline().rstrip().rsplit())
count = []
board = []

def compare_board(start_x:int,start_y:int,board:list):
    count = 0
    
    for i in range(start_y,start_y+8):
        for j in range(start_x,start_x+8):
            if board[i][j] != "BW"[(i+j)%2]:
                count += 1
        
    return count

for i in range(row):
    board.append(sys.stdin.readline().rstrip())

for i in range(row-7):
    for j in range(column-7):
        count_B = compare_board(j,i,board)
        count += [count_B,64-count_B]

print(min(count))