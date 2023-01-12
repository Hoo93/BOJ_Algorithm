import sys
from collections import deque

input = sys.stdin.readline

num = int(input().strip())
que = deque()

for _ in range(num):
    instruction = input().strip()
    if instruction[0:2] == "pu":
        que.append(instruction.split()[1])
    elif instruction[0:2] == "po":
        if len(que)== 0:
            print(-1)
        else:
            print(que.popleft())
    elif instruction[0:2] == "si":
        print(len(que))
    elif instruction[0:2] == "em":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif instruction[0:2] == "fr":
        if len(que) == 0 :
            print(-1)
        else:
            print(que[0])
    elif instruction[0:2] == "ba":
        if len(que) == 0 :
            print(-1)
        else:
            print(que[-1])
    