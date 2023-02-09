import sys

size = int(sys.stdin.readline().rstrip())
target = int(sys.stdin.readline().rstrip())

board = [ [ 0 for _ in range(size)] for _ in range(size)]
row,col = 0,0

for i in range(size,0,-2):
    start = i**2
    row,col = (size-1)//2-(i-1)//2,(size-1)//2 - (i-1)//2
    for j in range(i-1):
        board[row][col] = start
        start -= 1
        row += 1
    for j in range(i-1):
        board[row][col] = start
        start -= 1
        col += 1
    for j in range(i-1):
        board[row][col] = start
        start -= 1
        row -= 1
    for j in range(i-1):
        board[row][col] = start
        start -= 1
        col -= 1

row,col = (size-1)//2,(size-1)//2
board[row][col] = 1

for i in board:
    print(" ".join(map(str,i)))

for i in range(1,size+1,2):
    if i**2 >= target:
        size = i
        row -= (i-1)//2
        col -= (i-1)//2
        break

if size == 1:
    print(row+1,col+1)
else:
    q = (size**2 - target)//(size-1)
    r = (size**2 - target)%(size-1)
    
    row_list = [1,0,-1,0]
    col_list = [0,1,0,-1]
    
    for i in range(q):
        row += row_list[i]*(size-1)
        col += col_list[i]*(size-1)
    
    row += row_list[q]*r
    col += col_list[q]*r
    
    print(row+1,col+1)
