import sys
 
def is_promissing(floor:int)->bool:
    for index in range(1,floor):
        if col[index]==col[floor] or abs(col[index]-col[floor]) == floor - index:
            return False
    return True

def n_queen(floor:int):
    global cnt
    if floor == depth:
        cnt += 1
    else:
        for j in range(1,depth+1):
            col[floor+1] = j
            if is_promissing(floor+1):
                n_queen(floor+1)

depth =int(sys.stdin.readline().strip())
col = [0]*(depth+1)
cnt = 0
n_queen(0)
print(cnt)
    
