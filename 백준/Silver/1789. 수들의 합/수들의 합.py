import sys
import math
sys.setrecursionlimit(10**7)
num = int(sys.stdin.readline().rstrip())
n = int(math.sqrt(2*num))

if n*(n+1)//2 <= num:
    print(n)
else:
    print(n-1)