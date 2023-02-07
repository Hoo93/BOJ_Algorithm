import sys

row,col = map(int,sys.stdin.readline().rstrip().split())

size = min(row,col)

board = []

for _ in range(row):
    board.append(sys.stdin.readline().rstrip())

def get_max(size):
    for length in range(size,0,-1):
        for i in range(row-length+1):
            for j in range(col-length+1):
                if board[i][j] == board[i][j+length-1] == board[i+length-1][j] == board[i+length-1][j+length-1]:
                    return length

print(get_max(size)**2)