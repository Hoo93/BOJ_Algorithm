import sys
import itertools
sys.setrecursionlimit(10**7)

n,m = map(int,sys.stdin.readline().rstrip().split())
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)] 
chickens = []
house = []

for row in range(n):
    for col in range(n):
        if board[row][col] == 0:
            continue
        if board[row][col] == 1:
            house.append((row,col))
        elif board[row][col] == 2:
            chickens.append((row,col))

dp = [[2*n for _ in range(len(house))] for _ in range(len(chickens)) ]

for i in range(len(chickens)):
    for j in range(len(house)):
        dp[i][j] = abs(chickens[i][0]-house[j][0]) +abs(chickens[i][1]-house[j][1])

result = 10**7
for i in itertools.combinations(range(len(chickens)),m):
    tmp = 0
    for j in range(len(house)):
        mn = 10**7
        for k in i:
            mn = min(dp[k][j],mn)
        tmp += mn
    result = min(tmp,result)

print(result)