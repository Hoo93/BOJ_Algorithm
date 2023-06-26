import sys

# f = open("pratice.txt","r")
f = sys.stdin

N,m,M,T,R = map(int,f.readline().rstrip().split())
current = m
workout = 0
result = 0
if m + T > M:
    print(-1)
else:
    while True:
        result += 1
        if current + T <= M:
            current += T
            workout += 1
        else:
            current -= R
            if current < m:
                current = m
        if workout >= N:
            break

    print(result)