import sys
import heapq

N, M = map(int, sys.stdin.readline().rstrip().split())

basket = [i for i in range(N + 1)]
for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    basket[num1], basket[num2] = basket[num2], basket[num1]

print(" ".join(map(str, basket[1:])))
