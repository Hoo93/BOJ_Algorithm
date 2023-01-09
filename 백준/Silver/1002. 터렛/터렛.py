import sys
import math

input = sys.stdin.readline

case_num = int(input().strip())

def getDistance(a:list,b:list):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def getNode(a:list,b:list):
    distance = getDistance(a,b)
    max_rad = max(a[2],b[2])
    min_rad = min(a[2],b[2])


    if distance == 0:
        if max_rad == min_rad:
            return -1
        else:
            return 0
    if max_rad + min_rad == distance or max_rad - min_rad == distance:
        return 1
    if max_rad + min_rad < distance:
        return 0
    if max_rad - min_rad > distance:
        return 0
    if max_rad - min_rad == distance:
        return 1
    if max_rad + min_rad > distance:
        return 2 

for _ in range(case_num):
    points = list(map(int,input().rstrip().rsplit()))
    print(getNode(points[:3],points[3:]))