import sys

input = sys.stdin.readline

num = int(input().rstrip())

num_list = sorted(map(int,input().rstrip().rsplit()))
if num%2 == 1:
    print(num_list[num//2]**2)
else:
    print(num_list[0]*num_list[-1])