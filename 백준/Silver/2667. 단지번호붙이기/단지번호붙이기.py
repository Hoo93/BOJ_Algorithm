import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

size = int(sys.stdin.readline().rstrip())

square =["0"*(size+2)]+ ["0"+ sys.stdin.readline().rstrip() + "0" for _ in range(size)] + ["0"*(size+2)]
visited = [[False for _ in range(size+2)] for _ in range(size+2) ]
que = deque()
result = []
for i in range(1,size+1):
    for j in range(1,size+1):
        if square[i][j] == "1" and not visited[i][j]:
            count = 0
            que.append((i,j))

            while que:
                y,x = que.popleft()
                if visited[y][x]:
                    continue
                visited[y][x] = True
                count += 1
                if square[y+1][x] == "1": que.append((y+1,x))
                if square[y-1][x] == "1": que.append((y-1,x))
                if square[y][x+1] == "1": que.append((y,x+1))
                if square[y][x-1] == "1": que.append((y,x-1))
            
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)
