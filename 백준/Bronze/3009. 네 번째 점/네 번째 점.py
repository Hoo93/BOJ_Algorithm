import sys
input = sys.stdin.readline

x1,y1 = map(int,input().rsplit())
x2,y2 = map(int,input().rsplit())
x3,y3 = map(int,input().rsplit())

answer = ""
if x2 == x1:
    answer += str(x3)
else:
    if x2==x3:
        answer += str(x1)
    else:
        answer += str(x2)

if y2 == y1:
    answer += " "+str(y3)
else:
    if y2==y3:
        answer += " "+str(y1)
    else:
        answer += " "+str(y2)

print(answer)