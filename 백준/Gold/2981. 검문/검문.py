import sys
import math
num = int(sys.stdin.readline().strip())
num_list = []
answer = set()

num_list = [int(sys.stdin.readline().strip()) for _ in range(num)]
num_list.sort()
nlt = []

for i in range(num-1):
    nlt.append(num_list[i+1]-num_list[i])

gcd = nlt[0]
if num <=2:
    for i in range(2,int(math.sqrt(gcd))+1):
        if gcd%i == 0:
            answer.add(gcd//i)
            answer.add(i)
else:
    for i in range(1,num-1):
        gcd = math.gcd(gcd,nlt[i])

    for i in range(2,int(math.sqrt(gcd))+1):
        if gcd%i == 0:
            answer.add(i)
            answer.add(gcd//i)

answer.add(gcd)

for i in sorted(answer):
    print(i,end=" ")