import sys
from itertools import permutations
import re

# file = open('prac.txt','r')
# input = file.readline

input = sys.stdin.readline

pattern = r'(1[0]{2,}[1]{1,}|01)+'

N = int(input().strip())

for _ in range(N):
    N = input().rstrip()
    if re.fullmatch(pattern,N):
        print("YES")
    else:
        print("NO")
