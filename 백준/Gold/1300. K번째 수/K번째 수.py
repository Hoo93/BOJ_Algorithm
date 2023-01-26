import sys

input = sys.stdin.readline

size = int(input().rstrip())
k = int(input().rstrip())

left = 1
right = size**2
tmp = 0
while left <= right :
    mid = (left+right)//2

    cnt = 0
    for i in range(1,size+1):
        cnt += min(mid//i,size)
    
    if cnt >= k:
        tmp = mid
        right = mid - 1
    else:
        left = mid + 1

print(tmp)