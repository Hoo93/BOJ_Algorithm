import sys
from collections import deque
import copy

sys.setrecursionlimit(10**7)

# delta = [(1,0),(-1,0),(0,-1),(0,1)]
# size,length = map(int,sys.stdin.readline().rstrip().split())
# board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(size)]

sentence = sys.stdin.readline().rstrip()
answer = ""
tmp = ""
idx = 0
while idx < len(sentence):
    if sentence[idx] == "<":
        answer += tmp[::-1]
        tmp = "<"
        idx += 1
        while True:
            tmp += sentence[idx]
            if sentence[idx] == ">":
                answer += tmp
                tmp = ""
                idx += 1
                break
            else: idx += 1
    elif sentence[idx] == " ":
        answer += tmp[::-1] + " "
        tmp = ""
        idx += 1
    
    else:
        tmp += sentence[idx]
        idx += 1

answer += tmp[::-1]
print(answer)