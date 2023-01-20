import sys

input = sys.stdin.readline

size = int(input().rstrip())

count_blue = 0
count_white = 0

def slice(square,size:int)->int:
    global count_blue
    global count_white
    result = sum(square[0])
    recall = False
    if result != 0 and result != size:
        recall = True

    if not recall:
        for i in range(1,size):
            if sum(square[i]) == result:
                continue
            else:
                recall = True
                break
    
    if recall:
        new_size = size // 2
        square_a = []
        square_b = []
        square_c = []
        square_d = []
        for i in range(new_size):
            square_a.append(square[i][:new_size])
            square_b.append(square[i][new_size:])
        for j in range(new_size,size):
            square_c.append(square[j][:new_size])
            square_d.append(square[j][new_size:])
        slice(square_a,new_size)
        slice(square_b,new_size)
        slice(square_c,new_size)
        slice(square_d,new_size)
    else:
        if result == 0:
            count_white += 1
        else:
            count_blue += 1

board = [ list(map(int,input().rstrip().split())) for _ in range(size) ]

slice(board,size)

print(count_white)
print(count_blue)