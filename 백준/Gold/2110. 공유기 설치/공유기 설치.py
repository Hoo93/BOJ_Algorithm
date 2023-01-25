import sys
import bisect

input = sys.stdin.readline

n,c = map(int,input().rstrip().split())
house_distance = []

for _ in range(n):
    house_distance.append(int(input().rstrip()))

house_distance.sort()

min_distance = 1
max_distance = house_distance[-1]
tmp = house_distance[0]

while min_distance <= max_distance:

    tmp = house_distance[0]
    count = 1
    mid = (min_distance + max_distance)//2
    for i in range(1,n):
        if house_distance[i] >= tmp + mid:
            tmp = house_distance[i]
            count += 1

    if count >= c:
        min_distance = mid + 1
    else:
        max_distance = mid - 1

print(max_distance)