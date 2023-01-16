import sys
import bisect

input = sys.stdin.readline

n = int(input())
c_L = list(map(int,input().split()))
result = [0] * len(c_L)
def bitonic(idx:int):
    t_L = [0]
    
    for i in range(idx):
        t = len(t_L)
        if c_L[i] >= c_L[idx]:
            continue
        tmp = bisect.bisect_left(t_L,c_L[i])
        if  tmp >= t:
            t_L.append(c_L[i])
        else:
            t_L[tmp] = c_L[i]
    
    t_R = [0]

    for i in range(n-1,idx,-1):
        
        t = len(t_R)
        if c_L[i] >= c_L[idx]:
            continue
        tmp = bisect.bisect_left(t_R,c_L[i])
        if tmp >= t :
            t_R.append(c_L[i])
        else:
            t_R[tmp] = c_L[i]

    return len(t_L) + len(t_R) -1


for i in range(len(c_L)):
    result[i] = bitonic(i)

print(max(result))