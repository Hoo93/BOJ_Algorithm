import sys

f = sys.stdin
# f = open("input.txt","r")

A = int(f.readline().rstrip())
B = int(f.readline().rstrip())
C = int(f.readline().rstrip())

def verfyTriangle(a,b,c):
    if (a + b + c) != 180:
        return "Error"
    
    if a == b and a == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return  "Isosceles"
    else:
        return "Scalene"
    
print(verfyTriangle(A,B,C))