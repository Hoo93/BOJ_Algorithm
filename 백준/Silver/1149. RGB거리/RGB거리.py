import sys
input = sys.stdin.readline

n = int(input().strip())
price_list = [ list(map(int,input().strip().split())) for _ in range(n) ]

cache = {}

def dfs(idx:int,RGB:int):
    if idx == n-1:
        return price_list[idx][RGB]
    if (idx,RGB) in cache:
        return cache[(idx,RGB)]
    else:
        cache[(idx,RGB)] = min(price_list[idx][RGB] + dfs(idx+1,(RGB+1)%3), price_list[idx][RGB] + dfs(idx+1,(RGB+2)%3))
        return cache[(idx,RGB)]

print(min(dfs(0,0),dfs(0,1),dfs(0,2)))