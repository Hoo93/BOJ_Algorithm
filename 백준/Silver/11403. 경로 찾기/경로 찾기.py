import sys

f = sys.stdin
# f = open("input.txt","r")

size = int(f.readline().rstrip())
graph = [ list(map(int,f.readline().rstrip().split())) for _ in range(size)]

# 경유지점
for i in range(size):
    # 시작
    for j in range(size):
        # 도착
        for k in range(size):
             if graph[j][i] and graph[i][k]:
                  graph[j][k] = 1

for i in graph:
     print(" ".join(map(str,i)))