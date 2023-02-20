import sys
import bisect

h,w = map(int,sys.stdin.readline().rstrip().split())
board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]
tmp_board = []

def four_way(w,h,mx):
    for i in range(h-1):
        tmp = sum(board[i][:3])
        mx = max(mx,tmp + max(board[i+1][0],board[i+1][1],board[i+1][2]))
        for j in range(1,w-2):
            tmp = tmp - board[i][j-1] + board[i][j+2]
            tmp_mx = max(board[i+1][j],board[i+1][j+1],board[i+1][j+2])
            mx = max(mx,tmp+tmp_mx)
    
    return mx

mx = 0
for i in range(h-1):
    tmp = sum(board[i][:2]) + sum(board[i+1][:2])
    mx = max(mx,tmp)
    for j in range(1,w-1):
        tmp = tmp - board[i][j-1] - board[i+1][j-1] + board[i][j+1] + board[i+1][j+1]
        mx = max(mx,tmp)

for i in range(h):
    tmp = sum(board[i][:4])
    mx = max(mx,tmp)
    for j in range(1,w-3):
        tmp = tmp - board[i][j-1] + board[i][j+3]
        mx = max(mx,tmp)

for i in range(h-1):
    tmp = sum(board[i][1:3]) + sum(board[i+1][:2])
    tmp_two = sum(board[i+1][1:3]) + sum(board[i][:2])
    mx = max(mx,tmp,tmp_two)
    for j in range(1,w-2):
        tmp = tmp - board[i][j] - board[i+1][j-1] + board[i][j+2] + board[i+1][j+1]
        tmp_two = tmp_two - board[i+1][j] - board[i][j-1] + board[i+1][j+2] + board[i][j+1]
        mx = max(mx,tmp,tmp_two)

mx = four_way(w,h,mx)

for i in zip(*board[::-1]):
    tmp_board.append(i)
board = tmp_board
tmp_board = []
w = len(board[0])
h = len(board)

for i in range(h):
    tmp = sum(board[i][:4])
    mx = max(mx,tmp)
    for j in range(1,w-3):
        tmp = tmp - board[i][j-1] + board[i][j+3]
        mx = max(mx,tmp)

for i in range(h-1):
    tmp = sum(board[i][1:3]) + sum(board[i+1][:2])
    tmp_two = sum(board[i+1][1:3]) + sum(board[i][:2])
    mx = max(mx,tmp,tmp_two)
    for j in range(1,w-2):
        tmp = tmp - board[i][j] - board[i+1][j-1] + board[i][j+2] + board[i+1][j+1]
        tmp_two = tmp_two - board[i+1][j] - board[i][j-1] + board[i+1][j+2] + board[i][j+1]
        mx = max(mx,tmp,tmp_two)

mx = four_way(w,h,mx)

for i in zip(*board[::-1]):
    tmp_board.append(i)
board = tmp_board
tmp_board = []
w = len(board[0])
h = len(board)

mx = four_way(w,h,mx)

for i in zip(*board[::-1]):
    tmp_board.append(i)
board = tmp_board
tmp_board = []
w = len(board[0])
h = len(board)

mx = four_way(w,h,mx)

print(mx)