import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
num_list = list(map(int,sys.stdin.readline().strip().split()))
sign_count = list(map(int,sys.stdin.readline().strip().split()))

max_num = -1e9-1
min_num = 1e9+1

def dfs(index:int,val:int,add:int,sub:int,mul:int,div:int):
    global max_num
    global min_num
    if index == n-1:
        if val < min_num: min_num = val
        if val > max_num: max_num = val
    else:
        if add > 0 :dfs(index+1,val+num_list[index+1],add-1,sub,mul,div)
        if sub > 0 :dfs(index+1,val-num_list[index+1],add,sub-1,mul,div)
        if mul > 0 :dfs(index+1,val*num_list[index+1],add,sub,mul-1,div)
        if div > 0 :
            if val >= 0: dfs(index+1,val//num_list[index+1],add,sub,mul,div-1)
            else: dfs(index+1,(-1)*(((-1)*val)//num_list[index+1]),add,sub,mul,div-1)

dfs(0,num_list[0],sign_count[0],sign_count[1],sign_count[2],sign_count[3])
print(max_num)
print(min_num)