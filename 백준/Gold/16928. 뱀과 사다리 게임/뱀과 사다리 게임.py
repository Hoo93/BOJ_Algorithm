import sys
from collections import deque

ladder,snake = map(int,sys.stdin.readline().rstrip().split())

snake_and_ladder = set()
move_dict =dict()

for _ in range(ladder+snake):
    start,end = map(int,sys.stdin.readline().rstrip().split())
    snake_and_ladder.add(start)
    move_dict[start] = end


que = deque()
que.append((1,0))
dp = [ 0 for _ in range(101)]
while que:
    point,distance = que.popleft()
    if point >= 100:
        print(distance)
        break
    
    if dp[point] != 0:
        continue

    if point in snake_and_ladder:
        point = move_dict[point]
    
    dp[point] = distance
    
    for i in range(1,7):
        que.append((point+i,distance+1))