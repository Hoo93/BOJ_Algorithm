import sys
num = int(sys.stdin.readline())

for _ in range(num): 
    k,n = map(int,input().strip().split())
    answer = 1
    k = min(k,n-k)
    for i in range(k):
        answer *= (n-i)
    
    for i in range(1,k+1):
        answer //= i
    
    print(answer)