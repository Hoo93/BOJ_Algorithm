import sys

N = sys.stdin.readline().rstrip()
M = int(sys.stdin.readline().rstrip())
L = int(N[:-2] + "00")

while True:
    if L % M == 0:
        break
    L += 1

print(str(L)[-2:])
