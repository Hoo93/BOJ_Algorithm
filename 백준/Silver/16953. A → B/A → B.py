import sys
import bisect

n,m = map(int,sys.stdin.readline().rstrip().split())

def dfs(num,cnt):
    if num == n:
        return cnt
    
    if num < n:
        return -1

    if num %10 == 1:
        return dfs(num//10,cnt+1)
    
    if num%2 == 0:
        return dfs(num//2,cnt+1)
    
    return -1
    
print(dfs(m,1))