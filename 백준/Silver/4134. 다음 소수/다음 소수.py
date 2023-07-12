import sys
import math
from bisect import bisect_right

f = sys.stdin
# f = open("input.txt","r")

prime = [3]

for i in range(5,int(math.sqrt(45*10**8)),2):
    idx = bisect_right(prime,math.sqrt(i))
    flag = True
    for j in range(idx):
        if i%prime[j] == 0:
            flag = False
            break
    if flag: prime.append(i)

for _ in range(int(f.readline().rstrip())):
    N = int(f.readline().rstrip())
    if N <= 2:
        print(2)
    else:
        if N % 2 == 0: 
            N += 1
        
        flag = True
        
        while flag:
            flag = False
            for idx in range(bisect_right(prime,math.sqrt(N))):
                if N % prime[idx] != 0:
                    continue
                else:
                    N += 2
                    flag = True
                    break
            
        print(N)
                    