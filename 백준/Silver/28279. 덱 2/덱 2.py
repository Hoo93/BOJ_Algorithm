from collections import deque
import sys

dq = deque()

N = int(sys.stdin.readline())

for i in range(N):
    instruction = sys.stdin.readline().strip()

    if instruction[0] == "1":
        dq.appendleft(int(instruction.split()[1]))
    elif instruction[0] == "2":
        dq.append(int(instruction.split()[1]))
    elif instruction[0] == "3":
        if dq:
            print(dq.popleft())
        else:
            print("-1")
    elif instruction[0] == "4":
        if dq:
            print(dq.pop())
        else:
            print("-1")
    elif instruction[0] == "5":
        print(len(dq))
    elif instruction[0] == "6":
        if dq:
            print("0")
        else:
            print("1")
    elif instruction[0] == "7":
        if dq:
            print(dq[0])
        else:
            print("-1")
    elif instruction[0] == "8":
        if dq:
            print(dq[-1])
        else:
            print("-1")
