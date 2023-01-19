import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
que = deque([i+1 for i in range(n)])
que.rotate
num_list = list(map(int,input().rstrip().split()))
count = 0

for num in num_list:
    idx = que.index(num)
    count += min(idx,len(que)-idx)
    que.rotate(-idx)
    que.popleft()

print(count)