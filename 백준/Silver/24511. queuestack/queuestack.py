import sys
from collections import deque

# file = open('input.txt','r')
#
# for line in file.readlines():
#     print(line.strip())

N = int(sys.stdin.readline())
dataStructures = list(map(int, sys.stdin.readline().split()))
numArr = list(map(int, sys.stdin.readline().split()))
inputLength = int(sys.stdin.readline())
inputArr = list(map(int, sys.stdin.readline().split()))

que = []
cnt = inputLength
for i in range(N-1 ,-1,-1):
    if not dataStructures[i]:
        que.append(numArr[i])
        cnt -= 1


if cnt >= 0:
    print(' '.join(map(str,que + inputArr[0:cnt])))
else:
    print(' '.join(map(str,que[:inputLength])))