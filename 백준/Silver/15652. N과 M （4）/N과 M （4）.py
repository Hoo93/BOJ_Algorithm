import sys
from itertools import combinations_with_replacement

n,m = map(int,sys.stdin.readline().rstrip().rsplit())
nums = ""
for i in range(1,n+1):
    nums += str(i)

print("\n".join(" ".join(number) for number in combinations_with_replacement(nums,m)))