import sys
import math

input = sys.stdin.readline
prime_num = 1000000007
mat = [[1,1],[1,0]]

def mul_matrix(a:list,b:list):
    changed = list(zip(*b))
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            tmp = 0
            for k in range(2):
                tmp += a[i][k]*changed[j][k]
            result[i][j] = tmp%prime_num
    return result

def suquare_matrix(a:list):
    changed = list(zip(*a))
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            tmp = 0
            for k in range(2):
                tmp += a[i][k]*changed[j][k]
            result[i][j] = tmp%prime_num
    return result

def involution_matrix(n:int):
    if n == 1:
        return mat
    else:
        if n % 2:
            return mul_matrix(suquare_matrix(involution_matrix((n-1)//2)),mat)
        else:
            return suquare_matrix(involution_matrix(n//2))

n = int(input().rstrip())
if n <= 2:
    print("1")
else:
    print(sum(involution_matrix(n-2)[0])%prime_num)