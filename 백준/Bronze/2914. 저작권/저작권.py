import sys

f = sys.stdin
# f = open("input.txt","r")
n,m = map(int,f.readline().rstrip().split())
print(n*(m-1)+1)
