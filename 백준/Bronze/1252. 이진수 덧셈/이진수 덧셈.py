import sys

f = sys.stdin
# f = open("input.txt","r")

a, b = f.readline().rstrip().split()

print(bin(int(a, 2) + int(b, 2))[2:])
