import sys
from collections import deque

# file = open('prac.txt','r')
# input = file.readline

input = sys.stdin.readline

M,N,K = map(int,input().rstrip().split())

boards = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().rstrip().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            boards[y][x] = 1

def bfs(x,y):
    if boards[y][x] == 1: return 0
    if x < 0 or x >= N: return 0
    if y < 0 or y >= M: return 0

    q = deque([(x,y)])

    area = 0

    while q:
        x1,y1 = q.popleft()
        if x1 < 0 or x1 >= N: continue
        if y1 < 0 or y1 >= M: continue
        if boards[y1][x1] == 1: continue 
        
        area += 1
        boards[y1][x1] = 1
        for dx in [1,-1]:
            q.append((x1+dx,y1))
        for dy in [1,-1]:
            q.append((x1,y1+dy))

    return area

results = []
            
for i in range(N):
    for j in range(M):
        area = bfs(i,j)
        if area > 0:
            results.append(area)

print(len(results))
results.sort()
print(" ".join(map(str,results)))
            


            