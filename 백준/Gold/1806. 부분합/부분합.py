import sys
import bisect

n,s = map(int,sys.stdin.readline().rstrip().split())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
prefix_sum = [ 0 for _ in range(n)]
result = n+1

tmp = 0
for i in range(n):
    num = num_list[i]
    tmp += num
    prefix_sum[i] = tmp

if prefix_sum[-1] < s:
    print(0)
else:
    for i in range(n):
        if prefix_sum[i] < s:
            continue
        dif = prefix_sum[i] - s +1
        result = min(result,i-bisect.bisect_left(prefix_sum,dif)+1)

    print(result)