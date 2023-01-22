import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
board = [ input().rstrip() for _ in range(n)] 

def is_square(board:list,size:int):
    tmp = board[0]
    if tmp == "0"*size or tmp == "1"*size:
        for i in range(1,size):
            if board[i] != tmp:
                return False
        return True
    else:
        return False
    
def slice_conquer(board:list,size:int):
    if size != 1:
        result = "("
        board_one = [ board[i][:size//2] for i in range(size//2)]
        board_two = [ board[i][size//2:] for i in range(size//2)]
        board_three = [ board[i][:size//2] for i in range(size//2,size)]
        board_four = [ board[i][size//2:] for i in range(size//2,size)]
    
        # print("one",board_one)
        # print("two",board_two)
        # print("three",board_three)
        # print("four",board_four)
    
        if is_square(board_one,size//2):
            if board_one[0][0] == "1":
                result += "1"
            else:
                result += "0"
        else:
            result += slice_conquer(board_one,size//2)
        
        if is_square(board_two,size//2):
            if board_two[0][0] == "1":
                result += "1"
            else:
                result += "0"
        else:
            result += slice_conquer(board_two,size//2)
        
        if is_square(board_three,size//2):
            if board_three[0][0] == "1":
                result += "1"
            else:
                result += "0"
        else:
            result += slice_conquer(board_three,size//2)
        
        if is_square(board_four,size//2):
            if board_four[0][0] == "1":
                result += "1"
            else:
                result += "0"
        else:
            result += slice_conquer(board_four,size//2)
        
        result += ")"

        if result == "(0000)":
            return "0"
        elif result == "(1111)":
            return "1"
        return result
    else:
        if board[0] == "0":
            return "0"
        else:
            return "1"

print(slice_conquer(board,n))