import sys

input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
nlt = [ list(map(int,input().rstrip().split())) for _ in range(n) ]
m,k = map(int,input().rstrip().split())
nlt_two = list(zip(*[list(map(int,input().rstrip().split())) for _ in range(m)]))

def get_sum(a:list,b:list):
    result = 0
    for i in range(len(a)):
        result += a[i]*b[i]    
    return result

result = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        result[i][j] = str(get_sum(nlt[i],nlt_two[j]))

for i in range(n):
    print(" ".join(result[i]))