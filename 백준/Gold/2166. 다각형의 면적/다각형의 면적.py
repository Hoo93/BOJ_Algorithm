import sys

f = sys.stdin
# f = open("practice.txt","r")

N = int(f.readline().rstrip())

points = [list(map(int,f.readline().rstrip().split())) for _ in range(N)]
points.append(points[0])

surface = 0
for i in range(N):
    surface += points[i][0]*points[i+1][1] - points[i][1]*points[i+1][0]

print(abs(surface)/2)

