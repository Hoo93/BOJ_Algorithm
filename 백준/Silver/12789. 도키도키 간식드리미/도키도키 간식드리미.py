import sys

f = sys.stdin
# f = open("input.txt","r")

size = int(f.readline().rstrip())
numList = list(map(int, f.readline().rstrip().split()))

stack = []
result = [0]
isPossible = True

stack.append(size + 1)

for num in numList:
    while stack and stack[-1] < num:
        if stack[-1] < result[-1]:
            isPossible = False
            break
        result.append(stack.pop())

    if not isPossible:
        break

    stack.append(num)

if isPossible:
    if stack[-1] > result[-1]:
        print("Nice")
    else:
        print("Sad")
else:
    print("Sad")
