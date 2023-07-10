import sys

f = sys.stdin
# f = open("input.txt","r")

def getGCD(a,b):
    if b > a:
        a,b = b,a
    
    while b != 0:
        a,b = b,a%b
    return a

N = int(f.readline().rstrip())
start = int(f.readline().rstrip())
pre = 0
post = int(f.readline().rstrip())
gcd = post - start
pre = post

for _ in range(N-2):
    post = int(f.readline().rstrip())
    gcd = getGCD(gcd,post-pre)

print((post - start)//gcd + 1 - N)
