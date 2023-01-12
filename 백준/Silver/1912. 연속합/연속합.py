import sys

input = sys.stdin.readline

n = int(input().strip())
nlt = list(map(int,input().strip().split()))

sum_lst = [nlt[0]]
for i in range(len(nlt)-1):
    sum_lst.append(max(sum_lst[i]+nlt[i+1],nlt[i+1]))

print(max(sum_lst))
