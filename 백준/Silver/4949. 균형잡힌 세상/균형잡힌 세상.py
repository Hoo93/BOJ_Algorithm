import sys

input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    stack = []
    answer = "yes"
    if sentence == ".":
        break
    for chr in sentence:
        if chr == "(":
            stack.append("(")
        elif chr == ")":
            if "(" not in stack:
                answer = "no"
                break
            elif stack[-1] != "(":
                answer = "no"
                break
            else:
                stack.pop()
        elif chr == "[":
            stack.append("[")
        elif chr == "]":
            if "[" not in stack:
                answer = "no"
                break
            elif stack[-1] != "[":
                answer = "no"
                break
            else:
                stack.pop()
        else:
            continue
    
    if answer == "no":
        print(answer)
    elif len(stack) != 0:
        print("no")
    else:
        print(answer)
    
