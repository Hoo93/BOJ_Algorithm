import sys

f = sys.stdin
# f = open("input.txt","r")

N,M = f.readline().rstrip().split()

result = 0
tmp = 0
for i in N:
    tmp += int(i)
for j in M:
    result += tmp*int(j)
    
print(result)