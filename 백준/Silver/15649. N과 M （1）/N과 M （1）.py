import sys
import itertools

n,m = map(int,sys.stdin.readline().rstrip().rsplit())
nums = [str(i) for i in range(1,n+1)]
permut = itertools.permutations(nums,m)

print("\n".join(" ".join(comb) for comb in permut))