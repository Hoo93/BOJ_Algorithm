import sys

input = sys.stdin.readline
# file = open("input.txt", "r")
# input = file.readline

n, m = map(int, input().strip().split())

board = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


def getMaxSurface(x, y):

    if board[y][x] != 1 or visited[y][x] == 1:
        return 0
    queue = [(y, x)]
    visited[y][x] = 1
    surface = 1

    while queue:
        cy, cx = queue.pop()
        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = dy + cy, dx + cx
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if board[ny][nx] != 1 or visited[ny][nx] == 1:
                continue
            queue.append((ny, nx))
            visited[ny][nx] = 1
            surface += 1

    return surface


mx = 0
paintCount = 0
for i in range(n):
    for j in range(m):
        surface = getMaxSurface(j, i)
        if surface:
            paintCount += 1
            mx = max(mx, surface)

print(paintCount)
print(mx)
