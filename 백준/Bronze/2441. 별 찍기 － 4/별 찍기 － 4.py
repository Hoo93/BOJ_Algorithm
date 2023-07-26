import sys

f = sys.stdin
# f = open("input.txt","r")

N = int(f.readline().rstrip())

for i in range(N):
    print(" "*i + "*"*(N-i))