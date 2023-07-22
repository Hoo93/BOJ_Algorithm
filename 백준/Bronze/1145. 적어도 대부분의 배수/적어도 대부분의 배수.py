import sys
from itertools import combinations

f = sys.stdin
# f = open("input.txt","r")

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b:
        a, b = b, a % b
    
    return a

numList = list(map(int,f.readline().rstrip().split()))
mn = 100000000
for n1,n2,n3 in combinations(range(len(numList)),3):
    lcm = (numList[n1]*numList[n2]) / gcd(numList[n1],numList[n2])
    lcm = (lcm * numList[n3] ) / gcd(lcm,numList[n3])
    if lcm < mn:
        mn = lcm

print(int(mn))
