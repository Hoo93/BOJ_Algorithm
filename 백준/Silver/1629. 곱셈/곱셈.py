import sys

input = sys.stdin.readline
a,b,c = map(int,input().rstrip().split())
result = 1

def mul_DAC(a,b):
    if b == 1:
        return a
    else:
        if b%2 == 0:
            return mul_DAC(a,b//2)**2%c
        else:
            return mul_DAC(a,(b-1)//2)**2*a%c

print(mul_DAC(a,b)%c)