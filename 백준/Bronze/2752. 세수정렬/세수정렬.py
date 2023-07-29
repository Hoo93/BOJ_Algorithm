import sys

f = sys.stdin
# f = open("input.txt","r")

for i in sorted(map(int,f.readline().rstrip().split())):
    print(i,end=" ")