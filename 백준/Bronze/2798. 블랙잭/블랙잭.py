import sys
from itertools import combinations

a,b = map(int,sys.stdin.readline().rstrip().rsplit())
num_list = list(map(int,sys.stdin.readline().rstrip().rsplit()))

comb_list = sorted(set(map(sum,combinations(num_list,3))))

def search(num_list:list,num:int)->int:
    left,right = 0,len(num_list)-1
    mid = (left+right)//2
    while right-left>1:
        mid = (left+right)//2
        if num_list[mid]==num:
            return num_list[mid]
        elif num_list[mid] <= num:
            left = mid
        else:
            right = mid-1
    if num_list[right] <= num:
        return num_list[right]
    else:
        return num_list[left]

print(search(comb_list,b))