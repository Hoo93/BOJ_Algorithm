import sys
from collections import deque

input = sys.stdin.readline

que = deque()

for _ in range(int(input().rstrip())):
    command = input().rstrip()
    if command[:2] == "pu":
        que.append(int(command.split()[1]))
    elif command[:2] == "po":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif command[:2] == "si":
        print(len(que))
    elif command[:2] == "em":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif command[:2] == "fr":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif command[:2] == "ba":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    