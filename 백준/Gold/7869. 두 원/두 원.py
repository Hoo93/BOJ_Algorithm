import sys
import math
def getDist(x1,y1,x2,y2):
    return math.sqrt((x1 - x2)**2+(y1 - y2)**2)

# let r1 >= r2
def getSurface(x1,y1,r1,x2,y2,r2):
    dist = getDist(x1,y1,x2,y2)
    if dist >= r1 + r2:
        return 0
    
    if dist + r2 <= r1:
        return math.pi*r2**2
    
    angle_1 = math.acos((r1**2 - dist**2 - r2**2)/(-2*r2*dist))
    angle_2 = math.acos((r2**2 - dist**2 - r1**2)/(-2*r1*dist))
    # print(angle_1,angle_2)
    # print(math.cos(angle_1),math.cos(angle_2))
    surface = r1**2*angle_2 +r2**2*angle_1 - r1**2*math.sin(2*angle_2)/2 - r2**2*math.sin(2*angle_1)/2
    return surface

#f = open("practice.txt","r")
f = sys.stdin

x1,y1,r1,x2,y2,r2 = map(float,f.readline().rstrip().split())
if r2 > r1:
    r1,r2 = r2,r1

print(f"{round(getSurface(x1,y1,r1,x2,y2,r2),3):.3f}")