import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split())) + [0]

count = 0

left,right = 0,0
tmp = nums[0]

while left < N and right < N:
    if  tmp == M:
        count += 1
        right += 1
        tmp += nums[right]
        continue
    
    if tmp < M:
        right += 1
        tmp += nums[right]
        continue

    if tmp > M:
        tmp -= nums[left]
        left += 1

print(count)

    