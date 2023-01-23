import sys

input = sys.stdin.readline

n,b = map(int,input().rstrip().split())
nlt = [ list(map(int,input().rstrip().split())) for _ in range(n) ]

def get_sum(a:list,b:list):
    result = 0
    for i in range(len(a)):
        result += a[i]*b[i]%1000   
    return result

def get_square_matrix(a:list):
    result = [[0 for _ in range(len(a))] for _ in range(len(a)) ]
    changed = list(zip(*a))
    for i in range(len(a)):
        for j in range(len(a)):
            result[i][j] = get_sum(a[i],changed[j])
    return result

def get_mul_matrix(a:list,b:list):
    result = [[0 for _ in range(len(a))] for _ in range(len(a)) ]
    changed = list(zip(*b))
    for i in range(len(a)):
        for j in range(len(a)):
            result[i][j] = get_sum(a[i],changed[j])
    return result

def get_involution_matrix(a:list,b:int):
    if b == 1:
        return a
    else:
        if b%2:
            return get_mul_matrix(get_involution_matrix(get_square_matrix(a),(b-1)//2),a)
        else:
            return get_involution_matrix(get_square_matrix(a),b//2)

result = get_involution_matrix(nlt,b)

for i in range(n):
    for j in range(n):
        result[i][j] = str(result[i][j]%1000)

for i in range(n):
    print(" ".join(result[i]))
