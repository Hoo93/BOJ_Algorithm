import sys
cnt = 0
 
def is_promissing(floor:int)->bool:
    for index in range(floor):
        if row[index]==row[floor] or abs(row[index]-row[floor]) == floor - index:
            return False
    return True

def n_queen(floor:int):
    global cnt
    if floor == depth:
        cnt += 1
    else:
        for j in range(depth):
            row[floor] = j
            if is_promissing(floor):
                n_queen(floor+1)

depth =int(sys.stdin.readline().strip())
row = [0]*depth
n_queen(0)
print(cnt)
    
