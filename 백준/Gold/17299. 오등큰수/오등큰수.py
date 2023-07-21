import sys
from collections import Counter

f = sys.stdin
# f = open("input.txt","r")


size = int(f.readline().rstrip())
numList = list(map(int,f.readline().rstrip().split()))

cnt = Counter(numList)
result = [-1 for _ in range(size)]
stack = [0]

for i in range(size):
    while stack and cnt[numList[stack[-1]]] < cnt[numList[i]]:
        result[stack.pop()] = numList[i]
    stack.append(i) 

for i in result:
    print(i,end=" ")