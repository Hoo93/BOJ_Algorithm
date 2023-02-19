import sys
import bisect

num = sys.stdin.readline().rstrip()

tmp = num[0]
cnt = 0
for char in num[1:]:
    if char == tmp:
        continue
    else:
        tmp = char
        cnt += 1

print((cnt+1)//2)