import sys

f = sys.stdin
# f = open("practice.txt","r")

sentence = list(f.readline().rstrip())
stack = []

for _ in range(int(f.readline().rstrip())):
    instruction = f.readline().rstrip()

    if instruction[0] == "P":
        sentence.append(instruction[2])

    elif instruction[0] == "L":
        if len(sentence) <= 0:
            continue
        stack.append(sentence.pop())

    elif instruction[0] == "D":
        if len(stack) <= 0:
            continue
        sentence.append(stack.pop())

    elif instruction[0] == "B":
        if len(sentence) <= 0:
            continue
        sentence.pop()
        

print("".join(sentence + stack[::-1]))
