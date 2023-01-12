import sys
import bisect

input = sys.stdin.readline

input()
compare_list = sorted(map(int,input().strip().split()))
input()
number_list = list(map(int,input().strip().split()))

answer = []

for num in number_list:
    if compare_list[bisect.bisect_right(compare_list,num)-1] == num:
        answer.append("1")
    else:
        answer.append("0")

print("\n".join(answer))