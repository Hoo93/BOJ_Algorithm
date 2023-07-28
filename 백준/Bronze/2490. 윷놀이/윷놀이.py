import sys

f = sys.stdin
# f = open("input.txt","r")

for _ in range(3):
    tmp = sum(map(int,f.readline().rstrip().split()))
    
    if tmp == 0:
        print("D")
    elif tmp == 1:
        print("C")
    elif tmp == 2:
        print("B")
    elif tmp == 3:
        print("A")
    else:
        print("E")