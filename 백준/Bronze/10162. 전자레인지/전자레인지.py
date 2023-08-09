import sys

f = sys.stdin
# f = open("input.txt", "r")

buttons = [300, 60, 10]

cookingTime = int(f.readline().rstrip())

result = []
for time in buttons:
    result.append(cookingTime // time)
    cookingTime %= time

if cookingTime != 0:
    print(-1)
else:
    print(" ".join(map(str, result)))
