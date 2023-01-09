import sys
import math
sys.stdin.readline()
num_list = list(map(int,input().strip().split()))

for number in num_list[1:]:
    gcd = math.gcd(number,num_list[0])
    print(num_list[0]//gcd,end="")
    print("/",end="")
    print(number//gcd,end="")
    print()