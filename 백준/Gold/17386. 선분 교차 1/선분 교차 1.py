import sys

def CCW(x1,y1,x2,y2,x3,y3):
    if (x3-x1)*(y2-y1) - (y3-y1)*(x2-x1) > 0:
        return -1
    else:
        return 1

f = sys.stdin
# f = open("practice.txt","r")

x1,y1,x2,y2 = map(int,f.readline().rstrip().split())
x3,y3,x4,y4 = map(int,f.readline().rstrip().split())

if CCW(x1,y1,x2,y2,x3,y3)*CCW(x1,y1,x2,y2,x4,y4) > 0:
    print(0)
else:
    if CCW(x3,y3,x4,y4,x1,y1)*CCW(x3,y3,x4,y4,x2,y2) > 0:
        print(0)
    else:
        print(1)
