import sys
import math
a,b = map(int,sys.stdin.readline().strip().split())
print(math.gcd(a,b))
print(math.lcm(a,b))