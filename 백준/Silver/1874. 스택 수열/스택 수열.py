import sys
from collections import deque

input = sys.stdin.readline

number = int(input().strip())

order = [ int(input().strip()) for _ in range(number) ]
nums = deque([i for i in range(1,number+1) ])

tmp = order[0]
stack = []
answer = []

for _ in range(order[0]):
    stack.append(nums.popleft())
    answer.append("+")

stack.pop()
answer.append("-")

for num in order[1:]:
    if num > tmp:
        for _ in range(num-tmp):
            stack.append(nums.popleft())
            answer.append("+")
        tmp = num
        stack.pop()
        answer.append("-")
    else:
        if stack.pop() == num :
            answer.append("-")
        else:
            answer.append("NO")
            break

if answer[-1] == "NO":
    print("NO")
else:
    print("\n".join(answer))
