import sys

def hanoi(start:int,destination:int,number:int,path:list):
    if number==1:
        path.append(str(start)+" "+str(destination))
    else:
        hanoi(start,6-start-destination,number-1,path)
        hanoi(start,destination,1,path)
        hanoi(6-start-destination,destination,number-1,path)

a = list()
hanoi(1,3,int(sys.stdin.readline().rstrip()),a)
print(len(a))
for path in a:
    print(path)
