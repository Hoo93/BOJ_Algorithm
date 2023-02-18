import sys
import itertools
sys.setrecursionlimit(10**7)

num = int(sys.stdin.readline().rstrip())
rope = [int(sys.stdin.readline().rstrip()) for _ in range(num)]
rope.sort()

result = 0

for i in range(num):
    result = max(result,rope[i]*(num-i))
print(result)