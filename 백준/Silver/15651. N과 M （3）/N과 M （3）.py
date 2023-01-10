import sys
from itertools import product

n,m = map(int,sys.stdin.readline().rstrip().rsplit())
nums = ""
for i in range(1,n+1):
    nums += str(i)


print("\n".join(" ".join(number) for number in product(nums,repeat=m)))