import sys
import copy
sys.setrecursionlimit(10**6)

# f = open("practice.txt","r")
# N = int(f.readline().rstrip())
# board = [ list(map(int,f.readline().rstrip().split())) for _ in range(N)]

N = int(sys.stdin.readline().rstrip())
board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

flag = (N+1) % 2 
tmp = 0
result = 0

def locateBishop(nboard,row,col):
    board = copy.deepcopy(nboard)

    n_row,n_col = row-1,col-1
    while 0 <= n_row and 0 <= n_col:
        board[n_row][n_col] = 0
        n_row -= 1
        n_col -= 1
    
    n_row,n_col = row-1,col+1
    while 0 <= n_row and n_col < N:
        board[n_row][n_col] = 0
        n_row -= 1
        n_col += 1
    
    n_row,n_col = row+1,col+1
    while n_row < N and n_col < N:
        board[n_row][n_col] = 0
        n_row += 1
        n_col += 1

    n_row,n_col = row+1,col-1
    while n_row < N and 0 <= n_col:
        board[n_row][n_col] = 0
        n_row += 1
        n_col -= 1
    
    return board

def findMaxBishop(board,row,col,cnt):
    global tmp
    if col >= N:
        row += 1
        col %= N
        col += flag
        col %= 2
        
    while row < N and board[row][col] == 0:
        col += 2 
        if col >= N:
            row += 1
            col %= N
            col += flag
            col %= 2
            
    if row == N:
        tmp = max(tmp,cnt)
        return
    
    findMaxBishop(locateBishop(board,row,col),row,col+2,cnt+1)
    findMaxBishop(board,row,col+2,cnt)

findMaxBishop(board,0,0,0)
result += tmp 
tmp = 0


findMaxBishop(board,0,1,0)
result += tmp
print(result)
