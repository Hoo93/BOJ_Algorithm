import sys
from itertools import permutations
import math
def isConvex(p1,p2,p3):
    if (p1+p3) * p2 >= math.sqrt(2)*p1*p3:
        return True
    else:
        return False
    
def isConvexGraph(p,idxs):
    if not isConvex(points[idxs[5]],points[idxs[6]],p):
        return False
    if not isConvex(points[idxs[6]],p,points[idxs[0]]):
        return False
    if not isConvex(points[idxs[1]],points[idxs[0]],p):
        return False
    
    for i in range(5):
        if not isConvex(points[idxs[i]],points[idxs[i+1]],points[idxs[i+2]]):
            return False
    
    return True
    


f = sys.stdin
# f = open("practice.txt","r")

points = list(map(int,f.readline().rstrip().split()))

result = 0

for i in permutations(range(1,8),7):
    if isConvexGraph(points[0],i):
        result += 1

print(result*8)
    