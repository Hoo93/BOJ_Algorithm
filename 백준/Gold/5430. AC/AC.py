import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
is_reverse = False

for _ in range(n):
    command = input().rstrip()
    length = int(input().rstrip())
    num_list = list((input().rstrip()[1:-1]+",").split(","))
    num_list.pop()

    front = 0
    back = 0
    command_list = command.replace("RR","").split("R")
    for i in command_list[0::2]:
        front += len(i)
    for i in command_list[1::2]:
        back += len(i)
    end = length-back

    if front + back > length:
        print("error")
    else:
        if (len(command) - front - back) % 2 == 0 :
            is_reverse = False
        else:
            is_reverse = True

        if is_reverse:
            print(f'[{",".join(reversed(num_list[front:end]))}]')
        else:
            print(f'[{",".join(num_list[front:end])}]')