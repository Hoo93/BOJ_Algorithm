import sys
import itertools

n,m = map(int,sys.stdin.readline().rstrip().rsplit())
nlt = itertools.permutations(range(1,n+1),m)

for permutation in nlt:
    for j in range(m):
        print(permutation[j],end=" ")
    print()
