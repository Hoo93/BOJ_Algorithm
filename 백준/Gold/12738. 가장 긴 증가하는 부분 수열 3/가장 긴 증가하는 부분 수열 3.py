import sys
import bisect
import copy

length = int(sys.stdin.readline().rstrip())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
lis = []

for num in num_list:
    length = len(lis)
    idx = bisect.bisect_left(lis,num)
    if idx == length:
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))