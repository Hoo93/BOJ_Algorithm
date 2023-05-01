import sys

# f = open("practice.txt", "r")
# instructions = f.readlines()
instructions = sys.stdin.readlines()

cities = int(instructions[0].rstrip())
buses = int(instructions[1].rstrip())

visited = [[-1 for _ in range(cities + 1)] for _ in range(cities + 1)]
costs = [[200000 for _ in range(cities + 1)] for _ in range(cities + 1)]

for i in range(cities + 1):
    costs[i][i] = 0

for i in range(2, buses + 2):
    depart, arrive, cost = map(int, instructions[i].rstrip().split())
    # To Do 경로 구현
    if cost < costs[depart][arrive]:
        costs[depart][arrive] = cost
        visited[depart][arrive] = depart

for k in range(1, cities + 1):
    for i in range(1, cities + 1):
        for j in range(1, cities + 1):
            if costs[i][k] + costs[k][j] < costs[i][j]:
                costs[i][j] = costs[i][k] + costs[k][j]
                visited[i][j] = k

for i in range(1, cities + 1):
    for j in range(1, cities + 1):
        if costs[i][j] >= 200000:
            costs[i][j] = 0

for i in costs[1:]:
    print(" ".join(map(str, i[1:])))


def getPath(depart, arrive):
    if visited[depart][arrive] == -1:
        return [0]
    else:
        stopby = visited[depart][arrive]
        if stopby == depart:
            return [depart]
        else:
            return getPath(depart, stopby) + getPath(stopby, arrive)


for i in range(1, cities + 1):
    for j in range(1, cities + 1):
        path = getPath(i, j)
        if path[0] == 0:
            print(0)
        else:
            path += [j]
            print(len(path), end=" ")
            print(" ".join(map(str, path)))
