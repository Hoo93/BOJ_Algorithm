import sys

input = sys.stdin.readline

input()
compare_list = set(map(int,input().strip().split()))
input()
number_list = list(map(int,input().strip().split()))

answer = []

for num in number_list:
    if num in compare_list:
        answer.append("1")
    else:
        answer.append("0")

print("\n".join(answer))