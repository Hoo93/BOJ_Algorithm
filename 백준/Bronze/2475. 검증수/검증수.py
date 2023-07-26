import sys

f = sys.stdin
# f = open("input.txt","r")
result = 0
for i in f.readline().rstrip().split():
    result += int(i)**2

print(result%10)