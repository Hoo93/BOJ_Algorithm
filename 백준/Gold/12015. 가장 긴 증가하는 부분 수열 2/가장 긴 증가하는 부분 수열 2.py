import sys
import bisect

input = sys.stdin.readline

input()

num_list = list(map(int,input().rstrip().split()))

result = []

for num in num_list:
    tmp = bisect.bisect_left(result,num)

    if tmp == len(result):
        result.append(num)
    else:
        result[tmp] = num

print(len(result))
