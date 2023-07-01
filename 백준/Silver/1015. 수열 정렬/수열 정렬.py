import sys

# f = open("practice.txt","r")
f = sys.stdin

N = int(f.readline().rstrip())
numList = []
result = [0 for _ in range(N)]
for idx,num in enumerate(map(int,f.readline().rstrip().split())):
    numList.append((num,idx))

for i,(num,idx) in enumerate(sorted(numList)):
    result[idx] = i

print(" ".join(map(str,result)))
