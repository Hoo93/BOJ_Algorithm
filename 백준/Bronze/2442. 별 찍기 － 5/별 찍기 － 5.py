import sys

f = sys.stdin
# f = open("input.txt","r")

size = int(f.readline().rstrip())

for i in range(size):
    print(" "*(size-1-i)+ "*"*i + "*" + "*"*i)