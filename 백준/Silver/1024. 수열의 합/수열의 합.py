import sys

sm, length = map(int, sys.stdin.readline().rstrip().split())
flg = True
for i in range(length, 101):
    idx = sm - i * (i - 1) // 2

    if idx < 0:
        break

    if idx % i == 0:
        flg = False
        idx //= i
        print(" ".join(map(str, range(idx, idx + i))))
        break

if flg:
    print(-1)
