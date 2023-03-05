import sys
from collections import deque
import copy

def move(y,x,dir):
    if dir == 0: x += 1
    elif dir == 1: y -= 1
    elif dir == 2: x -= 1
    elif dir == 3: y += 1
    return (y,x)
    
def dragon_curve(start,dir,gen):
    que = deque()
    dir_list = [dir]
    x,y = start
    board[y][x] = 1
    y,x = move(y,x,dir)
    board[y][x] = 1

    for _ in range(gen):
        tmp = copy.deepcopy(dir_list)
        tmp.reverse()
        for i in range(len(tmp)): tmp[i] = (tmp[i]+1)%4
        for d in tmp:
            y,x = move(y,x,d)
            if 0 <= x <= 100 and 0 <= y <= 100:
                board[y][x] = 1
            else:
                return
        dir_list += tmp


board = [[0 for _ in range(101)] for _ in range(101)]
# 0 1 2 3 동 북 서 남
num = int(sys.stdin.readline().rstrip())
instructions = []

for _ in range(num):
    x,y,dir,gen = map(int,sys.stdin.readline().rstrip().split())
    instructions.append(((x,y),dir,gen))

for instruction in instructions:
    dragon_curve(instruction[0],instruction[1],instruction[2])

result = 0
for row in range(100):
    for col in range(100):
        if board[row][col]:
            if board[row+1][col] and board[row][col+1] and board[row+1][col+1]: result += 1

print(result)