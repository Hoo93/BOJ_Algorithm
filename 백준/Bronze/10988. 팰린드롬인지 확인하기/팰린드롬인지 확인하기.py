import sys

N = sys.stdin.readline().rstrip()

if N == N[::-1]:
    print(1)
else:
    print(0)