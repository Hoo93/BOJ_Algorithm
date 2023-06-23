import sys

def CCW(x1,y1,x2,y2,x3,y3):
    if (x3-x1)*(y2-y1) - (y3-y1)*(x2-x1) > 0:
        return -1
    elif (x3-x1)*(y2-y1) - (y3-y1)*(x2-x1) == 0:
        return 0
    else:
        return 1

def geCrossedPoint(x1,y1,x2,y2,x3,y3,x4,y4):
    if x1 == x2:
        return x1,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    
    if x3 == x4:
        return x3,((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))

    result_x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    result_y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    return result_x,result_y

def shareOnePoint(x1,y1,x2,y2,x3,y3,x4,y4):
    if x1 == x3 and y1 == y3:
        print(1)
        print(x1,y1)
        return 
    if x1 == x4 and y1 == y4:
        print(1)
        print(x1,y1)
        return 
    if x2 == x3 and y2 == y3:
        print(1)
        print(x2,y2)
        return 
    if x2 == x4 and y2 == y4:
        print(1)
        print(x2,y2)
        return 

def isCrossed(x1,y1,x2,y2,x3,y3,x4,y4):
    ccw1 = CCW(x1,y1,x2,y2,x3,y3)
    ccw2 = CCW(x1,y1,x2,y2,x4,y4)
    ccw3 = CCW(x3,y3,x4,y4,x1,y1)
    ccw4 = CCW(x3,y3,x4,y4,x2,y2)

    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if ccw1 == 0 and ccw2 == 0:
            if (x1,y1) <= (x4,y4) and (x3,y3) <= (x2,y2):
                return True 
            else:
                return False
        else:
            return True
    
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        return True
    
    return False

def getCrossPoint(x1,y1,x2,y2,x3,y3,x4,y4):
    print(1)
    try:
        result_x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        result_y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        print(result_x,result_y)
    except:
        if (x1,y1) == (x4,y4):
            print(x1,y1)
        elif (x2,y2) == (x3,y3):
            print(x2,y2)
        

f = sys.stdin
# f = open("practice.txt","r")

x1,y1,x2,y2 = map(float,f.readline().rstrip().split())
if x1 > x2:
    x1,y1,x2,y2 = x2,y2,x1,y1
elif x1 == x2:
    if y1 > y2:
        x1,y1,x2,y2 = x2,y2,x1,y1

x3,y3,x4,y4 = map(float,f.readline().rstrip().split())
if x3 > x4:
    x3,y3,x4,y4 = x4,y4,x3,y3
elif x3 == x4:
    if y3 > y4:
        x3,y3,x4,y4 = x4,y4,x3,y3

if isCrossed(x1,y1,x2,y2,x3,y3,x4,y4):
    getCrossPoint(x1,y1,x2,y2,x3,y3,x4,y4)
else:
    print(0)