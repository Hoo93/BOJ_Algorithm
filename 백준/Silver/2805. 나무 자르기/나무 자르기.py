import sys

input = sys.stdin.readline

n,k = map(int,input().strip().split())
number_list = list(map(int,input().strip().split()))

left,right = 0,2000000000

while left <= right:
    mid = (left+right)//2
    total_length = sum([num-mid for num in number_list if num >= mid])
    if total_length < k:
        right = mid -1
    elif total_length >= k:
        left = mid + 1

print(right)