import sys
import itertools

n,m = map(int,sys.stdin.readline().rstrip().rsplit())
nums = [list(str(i)) for i in range(1,n+1)]
answer = [list(str(i)) for i in range(1,n+1)]

def rep_permut(a:list,b:list)->list:
    repetition_list = []
    for i in a:
        for j in b:
            repetition_list.append(i+j)
    return repetition_list

for _ in range(m-1):
    answer = rep_permut(answer,nums)

for i in answer:
    print(" ".join(i))