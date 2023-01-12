import sys
from collections import deque

input = sys.stdin.readline

num = int(input().strip())
stack = []

for _ in range(num):
    instruction = input().strip()
    if instruction[0:2] == "pu":
        stack.append(instruction.split()[1])
    elif instruction[0:2] == "po":
        if len(stack)== 0:
            print(-1)
        else:
            print(stack.pop())
    elif instruction[0:2] == "si":
        print(len(stack))
    elif instruction[0:2] == "em":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif instruction[0:2] == "to":
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack[-1])
    