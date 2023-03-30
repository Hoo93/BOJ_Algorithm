import sys
from itertools import combinations
from bisect import bisect_right

INF = 10**8

#f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
#instructions = f.readlines()
instructions = sys.stdin.readlines()

size, weights = map(int, instructions[0].rstrip().split())
num_list = list(map(int, instructions[1].rstrip().split()))
num_list_one = num_list[: size // 2]
num_list_two = num_list[size // 2 :]

sum_list_one = [0]
sum_list_two = [0]

for i in range(1, len(num_list_one) + 1):
    tmp = 0
    for j in combinations(num_list_one, i):
        sum_list_one.append(sum(j))

for i in range(1, len(num_list_two) + 1):
    tmp = 0
    for j in combinations(num_list_two, i):
        sum_list_two.append(sum(j))

sum_list_one.sort()
sum_list_two.sort()

result = 0
for num in sum_list_one:
    idx = bisect_right(sum_list_two, weights - num)
    result += idx

print(result)
