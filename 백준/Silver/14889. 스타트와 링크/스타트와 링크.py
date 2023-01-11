import sys
from itertools import combinations

n = int(sys.stdin.readline().strip())
players = [ i for i in range(1,n+1)]
status =[[0]*(n+1)] + [ [0] +list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]


def sumStatus(players_A:list):
    result = 0
    players_B = [ i for i in range(1,n+1)]
    for i in players_A:
        players_B.remove(i)
    
    for i in range(len(players_A)-1):
        for j in range(i+1,len(players_A)):
            result += status[players_A[i]][players_A[j]]
            result += status[players_A[j]][players_A[i]]
            result -= status[players_B[j]][players_B[i]]
            result -= status[players_B[i]][players_B[j]]
    return abs(result)

players_one = [[1] +list(j) for j in combinations([i for i in range(2,n+1)],(n//2 -1)) ]
min = 1e9
for i in players_one:
    difference = sumStatus(i)
    if difference < min: min = difference

print(min)
