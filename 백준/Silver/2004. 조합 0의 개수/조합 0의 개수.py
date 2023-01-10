import sys
n,m = map(int,sys.stdin.readline().rstrip().rsplit())
cnt = 0

def num_counter(num:int,divider:int)->int:
    cnt = 0 
    while num > 0:
        cnt += num//divider
        num //= divider
    return cnt

print(min(num_counter(n,5)-num_counter(m,5)-num_counter(n-m,5),num_counter(n,2)-num_counter(m,2)-num_counter(n-m,2)))