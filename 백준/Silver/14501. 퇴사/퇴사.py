import sys
import bisect

N = int(sys.stdin.readline())

schedule = [[0,0]]

for _ in range(N):
    schedule.append(list(map(int,sys.stdin.readline().rstrip().split())))

dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    day = i+schedule[i][0]-1
    if day <= N:
        for j in range(day,N+1):
            dp[j] = max(dp[j],dp[i-1] + schedule[i][1])
    else:
        continue

print(dp[N])