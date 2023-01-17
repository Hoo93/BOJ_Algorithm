import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
num_list = list(map(int,input().rstrip().split()))

rem_list = [0 for i in range(m)]
rem_list[0] = 1

accum = 0
for i in range(n):
    accum = (accum + num_list[i])%m
    rem_list[accum] += 1

result = 0
for num in rem_list:
    if num <= 1:
        continue
    else:
        result += num*(num-1)//2

print(result)