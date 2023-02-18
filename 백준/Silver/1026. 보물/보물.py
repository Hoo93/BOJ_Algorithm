import sys
import itertools
sys.setrecursionlimit(10**7)

length = int(sys.stdin.readline().rstrip())
a = sorted(map(int,sys.stdin.readline().rstrip().split()),reverse=True)
b = sorted(map(int,sys.stdin.readline().rstrip().split()))

result = 0
for i in range(length):
    result += a[i]*b[i]

print(result)