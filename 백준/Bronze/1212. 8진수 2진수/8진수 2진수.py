import sys

f = sys.stdin
# f = open("input.txt","r")

print(bin(int(f.readline().rstrip(),8))[2:])