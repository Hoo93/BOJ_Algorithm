import sys

def CCW(x1,y1,x2,y2,x3,y3):
    if (x3-x1)*(y2-y1) - (y3-y1)*(x2-x1) > 0:
        return -1
    elif (x3-x1)*(y2-y1) - (y3-y1)*(x2-x1) == 0:
        return 0
    else:
        return 1


def isCrossed(x1,y1,x2,y2,x3,y3,x4,y4):
    ccw1 = CCW(x1,y1,x2,y2,x3,y3)
    ccw2 = CCW(x1,y1,x2,y2,x4,y4)
    ccw3 = CCW(x3,y3,x4,y4,x1,y1)
    ccw4 = CCW(x3,y3,x4,y4,x2,y2)

    if ccw1 * ccw2 > 0:
        return 0
    elif ccw1 * ccw2 < 0:
        if ccw3 * ccw4 > 0:
            return 0
        else:
            return 1
    else:
        if ccw3 * ccw4 < 0:
            return 1
        elif ccw3 * ccw4 > 0:
            return 0
        else:
            if ccw1 == 0 and ccw2 == 0:
                if x1 == x2:
                    if y3 <= y2 and y1 <= y4:
                        return 1
                    else:
                        return 0
                else:
                    if x3 <= x2 and x1 <= x4:
                        return 1
                    else:
                        return 0
            else:
                return 1
                

f = sys.stdin
# f = open("practice.txt","r")

x1,y1,x2,y2 = map(int,f.readline().rstrip().split())
if x1 > x2:
    x1,y1,x2,y2 = x2,y2,x1,y1
elif x1 == x2:
    if y1 > y2:
        x1,y1,x2,y2 = x2,y2,x1,y1

x3,y3,x4,y4 = map(int,f.readline().rstrip().split())
if x3 > x4:
    x3,y3,x4,y4 = x4,y4,x3,y3
elif x3 == x4:
    if y3 > y4:
        x3,y3,x4,y4 = x4,y4,x3,y3

print(isCrossed(x1,y1,x2,y2,x3,y3,x4,y4))


