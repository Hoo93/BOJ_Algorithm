import sys

input = sys.stdin.readline

while True:
    nlt = list(map(int,input().rstrip().split()))
    number = nlt.pop(0)

    if number == 0:
        break

    answer = 0
    stack = []

    for idx in range(number):
        while len(stack) != 0 and nlt[stack[-1]] > nlt[idx]:
            tmp = stack.pop()
            
            if len(stack) == 0:
                width = idx
            else:
                width = idx - stack[-1] - 1
            
            answer = max(answer, width*nlt[tmp])
        stack.append(idx)
    
    while len(stack) != 0:
            tmp = stack.pop()
            
            if len(stack) == 0:
                width = number
            else:
                width = number - stack[-1] - 1
            
            answer = max(answer, width*nlt[tmp])
    
    print(answer)