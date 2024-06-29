import sys

input = sys.stdin.readline
# file = open("input.txt", "r")
# input = file.readline

r, c = map(int, input().strip().split())

board = [input().rstrip() for _ in range(r)]
visited = [["." for _ in range(c)] for _ in range(r)]
delta = ((1, 0), (-1, 0), (0, 1), (0, -1))


def findJ():
    for i in range(r):
        for j in range(c):
            if board[i][j] == "J":
                return [(i, j)]


def findFire():
    result = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == "F":
                result.append((i, j))

    return result


# Jihoon Queue One Cicle
# dy,dx BFS Start
# Not Using Visited
# Change Board
# Then BFS fireQueue One Cicle


def bfs():
    jihoonQueue = findJ()
    fireQueue = findFire()

    distance = 1
    while jihoonQueue:

        nJihoonQueue = []
        while jihoonQueue:
            y, x = jihoonQueue.pop()
            if visited[y][x] == "F":
                continue

            for dy, dx in delta:
                ny, nx = dy + y, dx + x
                if ny < 0 or nx < 0 or nx >= c or ny >= r:
                    return distance
                if board[ny][nx] != "." or visited[ny][nx] != ".":
                    continue
                visited[ny][nx] = "J"
                nJihoonQueue.append((ny, nx))
        jihoonQueue = nJihoonQueue

        nFireQueue = []
        while fireQueue:
            y, x = fireQueue.pop()

            for dy, dx in delta:
                ny, nx = dy + y, dx + x
                if ny < 0 or nx < 0 or nx >= c or ny >= r:
                    continue
                if board[ny][nx] != "." or visited[ny][nx] == "F":
                    continue
                visited[ny][nx] = "F"
                nFireQueue.append((ny, nx))

        fireQueue = nFireQueue

        distance += 1

    return "IMPOSSIBLE"


print(bfs())
