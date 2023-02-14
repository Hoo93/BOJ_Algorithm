import sys

depth = int(sys.stdin.readline().rstrip())

row = [0 for _ in range(depth)]
cnt = 0

# is_possisble col을 대입하면 현재 row와 비교해 가능한지 출력
def check(row,col):
    length = len(row)
    if col in row:
        return False
    for i in range(len(row)):
        if row[length-i-1] == col - i-1:
            return False
        elif row[length-i-1] == col + i+1:
            return False
    return True

def nqueen(row:list,floor):
    global cnt
    if floor == depth-1:
        cnt += 1
    else:
        for i in range(depth):
            if check(row,i):
                nqueen(row+[i],floor+1)
            
for i in range(depth):
    nqueen([i],0)

print(cnt)