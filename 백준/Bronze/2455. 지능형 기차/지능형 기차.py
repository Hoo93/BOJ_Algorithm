import sys

f = sys.stdin
# f = open("input.txt","r")
tmp = 0
mx = 0
for _ in range(4):
    checkOut,checkIn = map(int,f.readline().rstrip().split())
    tmp = tmp+checkIn-checkOut
    mx = max(mx,tmp)

print(mx)
