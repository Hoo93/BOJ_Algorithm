import sys
from collections import deque
import copy

size = int(sys.stdin.readline().rstrip())
board = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(size)]
mx = 0

def move(board,dir:int):
    tmp = deque()
    result = deque()
    # 북쪽으로 이동
    if dir == 0:
        for col in range(size):
            tmp.clear()
            result.clear()
            
            for row in range(size):
                if board[row][col] == 0: continue
                tmp.append(board[row][col])
            tmp.append(0)
            
            while len(tmp) > 1:
                if tmp[0] == tmp[1]: result.append(tmp.popleft()+tmp.popleft())
                else: result.append(tmp.popleft())
            
            idx = len(result)
            for i in range(idx): board[i][col] = result[i]
            for i in range(idx,size): board[i][col] = 0
    
    # 남쪽으로 이동 
    if dir == 2:
        for col in range(size):
            tmp.clear()
            result.clear()
            
            for row in range(size-1,-1,-1):
                if board[row][col] == 0: continue
                tmp.append(board[row][col])
            tmp.append(0)
            
            while len(tmp) > 1:
                if tmp[0] == tmp[1]: result.append(tmp.popleft()+tmp.popleft())
                else: result.append(tmp.popleft())
            
            idx = len(result)
            for i in range(idx): board[size-1-i][col] = result[i]
            for i in range(size-idx): board[i][col] = 0
    
    # 동쪽으로 이동
    if dir == 1:
        for row in range(size):
            tmp.clear()
            result.clear()

            for col in range(size-1,-1,-1):
                if board[row][col] != 0: tmp.append(board[row][col])
            tmp.append(0)
            while len(tmp) > 1:
                if tmp[0] == tmp[1]: result.append(tmp.popleft()+tmp.popleft())
                else: result.append(tmp.popleft())
            
            idx = len(result)
            for i in range(idx): board[row][size-1-i] = result[i]
            for i in range(size-idx): board[row][i] = 0

    if dir == 3:
        for row in range(size):
            tmp.clear()
            result.clear()

            for col in range(size):
                if board[row][col] != 0: tmp.append(board[row][col])
            tmp.append(0)
            while len(tmp) > 1:
                if tmp[0] == tmp[1]: result.append(tmp.popleft()+tmp.popleft())
                else: result.append(tmp.popleft())

            idx = len(result)
            for i in range(idx): board[row][i] = result[i]
            for i in range(idx,size): board[row][i] = 0
    
    return board

def dfs(board,cnt):
    global mx
    if cnt == 5:
        for i in board:
            mx = max(max(i),mx)
    else:
        for i in range(4):
            nboard = copy.deepcopy(board)
            dfs(move(nboard,i),cnt+1)

dfs(board,0)
print(mx)