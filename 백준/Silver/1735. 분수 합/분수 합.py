import sys
from collections import deque

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
# instructions = map(int,sys.stdin.readline().rstrip())


def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b


a, b = map(int, sys.stdin.readline().rstrip().split())
c, d = map(int, sys.stdin.readline().rstrip().split())

numerator = a * d + b * c
denominator = b * d

n = gcd(numerator, denominator)
print(numerator // n, denominator // n)
