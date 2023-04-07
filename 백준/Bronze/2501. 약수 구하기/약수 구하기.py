import sys
from collections import deque

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
# instructions = map(int,sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())

count = 1
if b == 1:
    print(1)
else:
    result = 0
    for i in range(2, a + 1):
        if a % i == 0:
            count += 1
            if count == b:
                result = i
                break
    print(result)
