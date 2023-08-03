import sys

f = sys.stdin
# f = open("input.txt","r")

stack = []

for _ in range(int(f.readline().rstrip())):
    instruction = f.readline().rstrip().split()

    if instruction[0] == "1":
        stack.append(int(instruction[1]))
    elif instruction[0] == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif instruction[0] == "3":
        print(len(stack))
    elif instruction[0] == "4":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
