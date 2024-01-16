import sys

def hanoi(start:int,destination:int,number:int):
    if number==1:
        path.append(str(start)+" "+str(destination))
    else:
        hanoi(start,6-start-destination,number-1)
        hanoi(start,destination,1)
        hanoi(6-start-destination,destination,number-1)

path = list()
hanoi(1,3,int(sys.stdin.readline().rstrip()))
print(len(path))
for p in path:
    print(p)
