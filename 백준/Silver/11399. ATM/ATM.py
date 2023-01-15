import sys

input = sys.stdin.readline

input()

nlt = list(map(int,input().rstrip().split()))

nlt.sort(reverse=True)
answer = 0 
for i in range(len(nlt)):
    answer += (i+1)*nlt[i]

print(answer)
