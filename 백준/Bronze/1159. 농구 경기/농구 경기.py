import sys
from itertools import combinations

f = sys.stdin
# f = open("input.txt","r")

N = int(f.readline().rstrip())

alpha = [ 0 for _ in range(26) ]

for _ in range(N):
    name = f.readline().rstrip()
    alpha[ord(name[0]) - 97] += 1

result = ""
for i in range(26):
    if alpha[i] >= 5:
        result += chr(i + 97)

if result == "":
    print("PREDAJA")
else:
    print(result)