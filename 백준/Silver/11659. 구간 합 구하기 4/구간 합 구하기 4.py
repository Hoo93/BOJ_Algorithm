import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
num_list = [0] + list(map(int,input().rstrip().split()))
sum_list = []
tmp = 0
for i in range(n+1):
    tmp += num_list[i]
    sum_list.append(tmp)


for _ in range(m):
    start,end = map(int,input().rstrip().split())
    print(sum_list[end] - sum_list[start-1])