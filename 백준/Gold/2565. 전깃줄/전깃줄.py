import sys
import bisect

input = sys.stdin.readline

n = int(input())
line = [list(map(int,input().split())) for _ in range(n)]
line.sort(key=lambda x :x[0])

t_L = [0]
for i in range(len(line)):
    
    tmp = bisect.bisect_left(t_L,line[i][1])
    length = len(t_L)
    if tmp >= length:
        t_L.append(line[i][1])
    else:
        t_L[tmp] = line[i][1]

print(len(line) - len(t_L) +1)