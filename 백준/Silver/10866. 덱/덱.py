import sys
from collections import deque

input = sys.stdin.readline

num = int(input().strip())
que = deque()

for _ in range(num):
    instruction = input().strip()
    if "push_front" in instruction:
        que.appendleft(instruction.split()[1])
    elif "push_back" in instruction:
        que.append(instruction.split()[1])
    elif "pop_front" in instruction:
        if len(que)== 0:
            print(-1)
        else:
            print(que.popleft())
    elif "pop_back" in instruction:
        if len(que)== 0:
            print(-1)
        else:
            print(que.pop())
    elif "size" in instruction:
        print(len(que))
    elif "empty" in instruction:
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif "front" in instruction:
        if len(que) == 0 :
            print(-1)
        else:
            print(que[0])
    elif "back" in instruction:
        if len(que) == 0 :
            print(-1)
        else:
            print(que[-1])
    