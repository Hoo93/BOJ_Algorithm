import sys

# format = cmd + opt + L

# file = open('input.txt', 'r')
# input = file.readline

input = sys.stdin.readline

N, S = map(int, input().strip().split())

nums = sorted(map(int, input().strip().split()))

result = 0

def backTracking(index: int, sum: int):
    global result
    if index == N and sum == S:
        result += 1
    if index >= N:
        return
    if sum > S and nums[index] > 0:
        return

    backTracking(index + 1, sum)
    backTracking(index + 1, sum + nums[index])


backTracking(0, 0)

if S == 0:
    result -= 1
print(result)
