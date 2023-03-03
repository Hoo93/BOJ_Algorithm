import sys
from collections import deque
import copy

sys.setrecursionlimit(10**7)

# delta = [(1,0),(-1,0),(0,-1),(0,1)]
size,length = map(int,sys.stdin.readline().rstrip().split())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(size)]

def check(row):
    tmp = board[row][0]
    stare = [True for _ in range(size)]
    for idx,num in enumerate(board[row]):
        if num == tmp: continue
        if abs(num - tmp) >= 2: return False
        if num > tmp:
            if idx - length < 0: return False
            for i in range(idx-length,idx):
                if board[row][i] == tmp and stare[i]:
                    stare[i] = False
                    continue
                return False
            tmp = num
        else:
            if idx + length -1 > size -1: return False
            for i in range(idx,idx+length):
                if board[row][i] == tmp-1 and stare[i]:
                    stare[i] = False
                    continue
                return False
            tmp = num
    return True
result = 0
for i in range(size):
    if check(i): result += 1

board = list(zip(*board))
for i in range(size):
    if check(i): result += 1

print(result)