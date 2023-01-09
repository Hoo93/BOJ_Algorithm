import sys
import math

input = sys.stdin.readline
points = []
index = 0
max_width = 0
max_height = 0

korean_melon = int(input().strip())

for _ in range(6):
    points.append(list(map(int,input().strip().split())))

for i in range(6):
    if points[i%6][0] == points[(i+2)%6][0] and points[(i+1)%6][0] == points[(i+3)%6][0]:
        index = i%6
        break

for i in range(3):
    if points[2*i][1] >= max_height:
        max_height = points[2*i][1]
    if points[2*i+1][1] >= max_width:
        max_width = points[2*i+1][1] 

print(korean_melon*(max_width*max_height-points[(index+1)%6][1]*points[(index+2)%6][1]))
