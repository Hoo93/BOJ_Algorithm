import sys
from collections import deque

sys.setrecursionlimit(10**8)

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
nums = sys.stdin.readlines()
for i in range(len(nums)):
    nums[i] = int(nums[i].rstrip())


def preToPost(nums: list) -> list:
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums
    root = nums[0]
    idx = 1
    while idx < len(nums):
        if nums[idx] > root:
            break
        else:
            idx += 1

    left = preToPost(nums[1:idx])
    right = preToPost(nums[idx:])

    return left + right + [root]


for num in preToPost(nums):
    print(num)
