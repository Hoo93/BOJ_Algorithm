import sys
import heapq
import bisect

# format = cmd + opt + L

#file = open('input.txt', 'r')
#input = file.readline

input = sys.stdin.readline

N, K = map(int, input().split())

# 보석의 무게와 가치
jewels = []
bags = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(jewels, (weight, value))

for _ in range(K):
    bags.append(int(input()))

bags.sort()

answer = 0
issued = [False for _ in range(K)]

available_jewels = []
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        weight, value = heapq.heappop(jewels)
        heapq.heappush(available_jewels,-value)

    if available_jewels:
        nValue = heapq.heappop(available_jewels)
        answer -= nValue

print(answer)
