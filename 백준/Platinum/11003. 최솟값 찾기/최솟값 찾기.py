import sys
from collections import deque
n,l = map(int,sys.stdin.readline().rstrip().split())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))

d = [ 0 for _ in range(n)]
dq = deque()

for idx in range(n):
    while dq and dq[-1][1] > num_list[idx]:
        dq.pop()
    
    while dq and idx - dq[0][0] >= l:
        dq.popleft()
    
    dq.append((idx,num_list[idx]))
    d[idx] = dq[0][1]

for i in d:
    print(i,end=" ")