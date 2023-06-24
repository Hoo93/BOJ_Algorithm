import sys

# f = open("pratice.txt","r")
f = sys.stdin

N,B = map(int,f.readline().strip().split())

result = ""

while N > 0:
    r = N%B
    N //= B
    if r >= 10:
        result += chr(r+55)
    else:
        result += str(r)

print(result[::-1])