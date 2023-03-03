import sys
from collections import deque
import copy

sys.setrecursionlimit(10**7)

# delta = [(1,0),(-1,0),(0,-1),(0,1)]
# row,col,time = map(int,sys.stdin.readline().rstrip().split())
# board = [[-1 for _ in range(col+2)]]+[[-1]+list(map(int,sys.stdin.readline().rstrip().split()))+[-1] for _ in range(row)]+[[-1 for _ in range(col+2)]] 

sentence = sys.stdin.readline().rstrip()
stack = []
tmp = 1
answer = 0
for i in range(len(sentence)):
    if sentence[i] == '(':
        stack.append(sentence[i])
        tmp *= 2
    
    elif sentence[i] == '[':
        stack.append(sentence[i])
        tmp *= 3
    
    elif sentence[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if sentence[i-1] == '(': answer += tmp
        tmp //= 2
        stack.pop()
    elif sentence[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if sentence[i-1] == '[': answer += tmp
        tmp //= 3
        stack.pop()

if stack: answer = 0

print(answer)