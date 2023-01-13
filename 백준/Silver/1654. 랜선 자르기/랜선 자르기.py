import sys

input = sys.stdin.readline

k,n = map(int,input().strip().split())
number_list = [ int(input().strip()) for _ in range(k)]

left,mid,right = 0,0,max(number_list)

while left <= right:
    mid = (left+right)//2
    if mid == 0:
        right = 1
        break
    num_of_wire = sum([num//mid for num in number_list])
    if num_of_wire < n:
        right = mid -1
    elif num_of_wire >= n:
        left = mid + 1

print(right)