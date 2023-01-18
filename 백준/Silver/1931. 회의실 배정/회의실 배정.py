import sys

input = sys.stdin.readline

n = int(input().rstrip())
meetings = [list(map(int,input().rstrip().split())) for _ in range(n)] 

meetings.sort(key= lambda x:x[1])
meetings.sort(key= lambda x:x[0])    
    
result = []
result.append(meetings[0])

for i in range(1,n):
    if meetings[i][1] < result[-1][1]:
        result[-1] = meetings[i]
    else:
        if meetings[i][0] >= result[-1][1]:
            result.append(meetings[i])
        else:
            continue

print(len(result))