import sys
input = sys.stdin.readline

n = int(input().strip())
num_list = [[int(input().strip())]]

for i in range(n-1):
    num_list.append(list(map(int,input().strip().split())))

cache = {}

def dfs(floor:int,idx:int):
    if floor == n-1:
        return num_list[floor][idx]
    if (floor,idx) in cache:
        return cache[(floor,idx)]
    else:
        cache[(floor,idx)] = max(num_list[floor][idx]+dfs(floor+1,idx),num_list[floor][idx]+dfs(floor+1,idx+1))
        return cache[(floor,idx)]

print(dfs(0,0))