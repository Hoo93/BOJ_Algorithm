import sys

f = sys.stdin
# f = open("input.txt","r")

N = int(f.readline().rstrip())

for i in range(N):
    print("*"*(i+1) + " "*2*(N-i-1) +"*"*(i+1))

for i in range(N-1):
    print("*"*(N-i-1) + " "*2*(i+1) + "*"*(N-i-1))