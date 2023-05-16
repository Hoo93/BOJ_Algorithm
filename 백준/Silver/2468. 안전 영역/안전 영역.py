import sys
from collections import deque

# f = open("practice.txt", "r")
# N = int(f.readline().rstrip())
# board = [list(map(int, f.readline().rstrip().split())) for _ in range(N)]
N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
delta = ((-1, 0), (1, 0), (0, 1), (0, -1))

mx_h = 0
for i in board:
    mx_h = max(mx_h, max(i))


def bfs(y, x, h, visited):
    que = deque()
    que.append((y, x))

    while que:
        y, x = que.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True

        for dy, dx in delta:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= N:
                continue
            if nx < 0 or nx >= N:
                continue
            if board[y][x] <= h:
                continue

            que.append((ny, nx))


def getCnt(h):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if board[i][j] <= h:
                continue
            cnt += 1
            bfs(i, j, h, visited)

    return cnt


def getSafearea(mx):
    result = 0
    for i in range(mx + 1):
        result = max(result, getCnt(i))

    return result


print(getSafearea(mx_h))
