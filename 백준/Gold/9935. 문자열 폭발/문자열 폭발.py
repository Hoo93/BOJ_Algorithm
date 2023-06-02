import sys

sentence = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()


stack = []
length = len(bomb)

for i in range(len(sentence)):
    stack.append(sentence[i])
    if ''.join(stack[-length:]) == bomb:
        for _ in range(length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')