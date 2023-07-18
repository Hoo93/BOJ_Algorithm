import sys

f = sys.stdin
# f = open("input.txt","r")

def verfyTriangle(a,b,c):
    if c >= a + b:
        return "Invalid"
    
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or c == a:
        return "Isosceles"
    else:
        return "Scalene"

while True:
    sentences = sorted(map(int,f.readline().rstrip().split()))
    if sum(sentences) == 0:
        break
    print(verfyTriangle(sentences[0],sentences[1],sentences[2]))