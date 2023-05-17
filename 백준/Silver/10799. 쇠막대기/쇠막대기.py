import sys

stack = []

sentence = sys.stdin.readline().rstrip()
sentence = sentence.replace("()", "l")
result = 0

for i in range(len(sentence)):
    if sentence[i] == "(":
        stack.append(sentence[i])
        result += 1
    elif sentence[i] == ")":
        stack.pop()
    else:
        result += len(stack)

print(result)
