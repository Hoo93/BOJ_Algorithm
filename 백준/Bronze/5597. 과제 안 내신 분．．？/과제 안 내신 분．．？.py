import sys

numList = [i for i in range(1,31) ]
for _ in range(28):
    numList.remove(int(sys.stdin.readline()))
print(numList[0])
print(numList[1])
