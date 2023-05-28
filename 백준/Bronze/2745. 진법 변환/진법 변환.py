import sys

sys.setrecursionlimit(10**6)
N, B = sys.stdin.readline().rstrip().split()
B = int(B)
num = 1
result = 0
for chr in N[::-1]:
    if ord(chr) >= 65:
        result += (ord(chr) - 55) * num
    else:
        result += (ord(chr) - 48) * num
    num *= B

print(result)
