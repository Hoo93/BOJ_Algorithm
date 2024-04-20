import sys
from itertools import permutations
input = sys.stdin.readline

ans = 0

N = int(input().strip())
nums = list(map(int, input().rstrip().split()))


def calDifference(iter):
    length = len(iter)
    result = 0
    for i in range(1,length):
        result += abs(nums[iter[i]] - nums[iter[i-1]])
    
    return result

for tup in permutations(range(N),N):
    ans = max(ans,calDifference(tup))

print(ans)
    





