import sys


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


a, b = map(int, sys.stdin.readline().rstrip().split())

print(a * b // get_gcd(a, b))
