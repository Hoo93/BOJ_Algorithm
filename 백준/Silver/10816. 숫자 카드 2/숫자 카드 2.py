import sys

sys.stdin.readline()
check = list(map(int,sys.stdin.readline().strip().split()))
sys.stdin.readline()
num_list = list(map(int,sys.stdin.readline().strip().split()))

d={}
answer = []
for num in check+num_list:
    d.update({num:0})
for num in check:
    d[num] += 1
for num in num_list:
    answer.append(d[num])
print(" ".join(map(str,answer)))
