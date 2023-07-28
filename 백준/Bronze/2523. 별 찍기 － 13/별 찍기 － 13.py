import sys

f = sys.stdin
# f = open("input.txt","r")

N = int(f.readline().rstrip())

for i in range(1,N+1):
    print("*"*i)
for i in range(N-1,0,-1):
    print("*"*i)