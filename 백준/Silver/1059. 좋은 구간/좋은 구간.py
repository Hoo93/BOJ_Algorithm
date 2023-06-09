import sys
from bisect import bisect_right

size = int(sys.stdin.readline().rstrip())
nlt = sorted(map(int,sys.stdin.readline().rstrip().split()))
num = int(sys.stdin.readline().rstrip())

if num in nlt:
    print(0)
else:
    idx = bisect_right(nlt,num)
    if idx != 0:
        mn = nlt[idx-1] + 1
        mx = nlt[idx] - 1
    else:
        mn = 1
        mx = nlt[0]-1
    result = 0
    for i in range(mn,num+1):
        result += mx - num + 1
    print(result-1)
