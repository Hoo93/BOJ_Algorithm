import sys
import heapq

input = sys.stdin.readline

number = int(input().rstrip())

hq = []

for _ in range(number):
    num = int(input().rstrip())
    if num != 0:
        heapq.heappush(hq,(abs(num),num))
    else:
        if len(hq) != 0:
            print(heapq.heappop(hq)[1])
        else:
            print("0")