import sys
from collections import deque

# format = cmd + opt + L

#file = open('input.txt', 'r')
#input = file.readline

input = sys.stdin.readline

WALL = '#'
PERSON = 'J'
FIRE = 'F'
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

row, col = map(int, input().strip().split())
boards = [input().strip() for _ in range(row)]

# Track fire spread time
fire_time = [[-1] * col for _ in range(row)]

fires = deque()
jihoon_start = None

for r in range(row):
    for c in range(col):
        if boards[r][c] == FIRE:
            fire_time[r][c] = 0
            fires.append((r, c))
        elif boards[r][c] == PERSON:
            jihoon_start = (r, c)

# Spread fire first
while fires:
    y, x = fires.popleft()

    for dy, dx in delta:
        ny, nx = y + dy, x + dx

        if 0 <= ny < row and 0 <= nx < col and boards[ny][nx] != WALL and fire_time[ny][nx] == -1:
            fire_time[ny][nx] = fire_time[y][x] + 1
            fires.append((ny, nx))


def bfs(start):
    q = deque([start])
    visited = [[-1] * col for _ in range(row)]
    visited[start[0]][start[1]] = 0

    while q:
        y, x = q.popleft()

        for dy, dx in delta:
            ny, nx = y + dy, x + dx

            # Jihoon escapes if reaching boundary
            if ny < 0 or ny >= row or nx < 0 or nx >= col:
                return visited[y][x] + 1

            if boards[ny][nx] == WALL or visited[ny][nx] != -1:
                continue

            # Only move if fire hasn't reached or if Jihoon reaches before fire
            if fire_time[ny][nx] == -1 or fire_time[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

    return 'IMPOSSIBLE'


# Start BFS for Jihoon
if jihoon_start:
    print(bfs(jihoon_start))
else:
    print('IMPOSSIBLE')