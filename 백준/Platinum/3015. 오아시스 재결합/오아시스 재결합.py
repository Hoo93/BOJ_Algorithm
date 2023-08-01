import sys

f = sys.stdin
# f = open("input.txt","r")

N = int(f.readline().rstrip())
stack = []
result = 0
for _ in range(N):
    num = int(f.readline().rstrip())

    while stack and stack[-1][0] < num:
        result += stack.pop()[1]

    if stack:
        if stack[-1][0] == num:
            cnt = stack.pop()[1]
            result += cnt
            if stack:
                result += 1
            stack.append((num, cnt + 1))
        else:
            result += 1
            stack.append((num, 1))

    else:
        stack.append((num, 1))

print(result)
