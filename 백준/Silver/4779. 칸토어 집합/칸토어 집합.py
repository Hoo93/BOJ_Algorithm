import sys
import math
from bisect import bisect_right

f = sys.stdin
# f = open("input.txt","r")

def recur(size:int):
    if size == 0:
        return "-"
    else:
        pre = recur(size-1)
        return pre + " "*3**(size-1) + pre
    
sizes = f.readlines()

for size in sizes:
    print(recur(int(size)))