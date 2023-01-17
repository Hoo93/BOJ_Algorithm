import sys
input = sys.stdin.readline

size,num = map(int,input().rstrip().split())

board = [[0]*(size+1)]+[ [0] +list(map(int,input().rstrip().split())) for _ in range(size) ]
prefix_board = [[0 for _ in range(size+1)] for _ in range(size+1)]

for row in range(1,size+1):
    accum = 0    
    for col in range(1,size+1):
        accum += board[row][col]
        prefix_board[row][col] = accum

for _ in range(num):
    result = 0
    y1,x1,y2,x2 = map(int,input().rstrip().split())
    for row in range(y1,y2+1):
        result += prefix_board[row][x2]-prefix_board[row][x1-1]
    print(result)