import sys

def print_sudoku():
    for i in range(9):
        print(" ".join(map(str,sudoku[i])))

def checkRow(a,b,num:int):
    if num in sudoku[a]:
        return False
    
    for i in range(9):
        if sudoku[i][b] == num:
            return False

    row = a//3
    col = b//3
    for i in range(3*(row),3*(row+1)):
        if num in sudoku[i][3*(col):3*(col+1)]:
            return False
    return True

def func_sudoku(index:int):
    if index == flag:
        print_sudoku()
        exit(0)
    else:
        row,col = empty[index]
        for num in num_set[row]:
            if checkRow(row,col,num):
                sudoku[row][col] = num
                func_sudoku(index+1)
                sudoku[row][col] = 0

sudoku =[list(map(int,sys.stdin.readline().strip().split())) for _ in range(9)]
# sudoku = [
#     [0,3,5,4,6,9,2,7,8],
#     [7,8,2,1,0,5,6,0,9],
#     [0,6,0,2,7,8,1,3,5],
#     [3,2,1,0,4,6,8,9,7],
#     [8,0,4,9,1,3,5,0,6],
#     [5,9,6,8,2,0,4,1,3],
#     [9,1,7,6,5,2,0,8,0],
#     [6,0,3,7,0,1,9,5,2],
#     [2,5,8,3,9,4,7,6,0]
# ]
number = set([1,2,3,4,5,6,7,8,9])
num_set = [ number - set(i) for i in sudoku ]
empty = []

for row in range(9):
    for col in range(9):
        if sudoku[row][col]==0:
            empty.append((row,col))
            
flag = len(empty)

func_sudoku(0)