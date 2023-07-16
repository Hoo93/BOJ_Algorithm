import sys
import math
from bisect import bisect_right

f = sys.stdin
# f = open("input.txt","r")
primes = [2]
for i in range(3,1000000,2):
    flag = True
    for idx in range(bisect_right(primes,math.sqrt(i))):
        if i % primes[idx] == 0:
            flag = False
            break
    if flag:
        primes.append(i)

for _ in range(int(f.readline().rstrip())):
    num = int(f.readline().rstrip())
    result = 0
    left_point = 0
    right_point = bisect_right(primes,num)

    while left_point <= right_point:
        if primes[left_point] + primes[right_point] == num:
            result += 1
            left_point += 1
            right_point -= 1
        elif primes[left_point] + primes[right_point] < num:
            left_point += 1
        else:
            right_point -= 1
    
    print(result)