import sys

input = sys.stdin.readline

case_num = int(input().strip())

def inPlanet(x:int,y:int,point:list)->bool:
    if (x-point[0])**2+(y-point[1])**2 < point[2]**2:
        return True
    else:
        return False


for _ in range(case_num):
    x1,y1,x2,y2 = map(int,input().rstrip().rsplit())
    planet_num = int(input().strip())
    count = 0
    for _ in range(planet_num):
        planet = list(map(int,input().strip().split()))
        if inPlanet(x1,y1,planet) ^ inPlanet(x2,y2,planet):
            count += 1
    
    print(count)