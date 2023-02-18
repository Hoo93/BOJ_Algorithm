import sys
import heapq
result = 0

numbers = [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))]
queue = []
tmp = 0

for num in numbers:
    heapq.heappush(queue,num)
tmp = heapq.heappop(queue)
while queue:
    tmp += heapq.heappop(queue)
    result += tmp
    heapq.heappush(queue,tmp)
    tmp = heapq.heappop(queue)

print(result)