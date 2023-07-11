import sys

f = sys.stdin
# f = open("input.txt","r")

total,p1,p2 = map(int,f.readline().rstrip().split())
rounds = 0

while True:
    if p1 == p2:
        break
    rounds += 1
    total = (total+1)//2
    p1 = (p1 + 1)//2
    p2 = (p2 + 1)//2

print(rounds)