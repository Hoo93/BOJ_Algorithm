import sys

f = sys.stdin
# f = open("input.txt","r")
mn_x,mx_x = 100000,-100000
mn_y,mx_y = 100000,-100000
for _ in range(int(f.readline().rstrip())):
    x,y = map(int,f.readline().rstrip().split())
    if x < mn_x:
        mn_x = x
    if x > mx_x:
        mx_x = x
    if y < mn_y:
        mn_y = y
    if y > mx_y:
        mx_y = y

print((mx_x - mn_x)*(mx_y - mn_y))