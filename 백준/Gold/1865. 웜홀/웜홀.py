import sys

# format = cmd + opt + L

input = sys.stdin.readline

INF = 1e9

def bellman_ford():
    for i in range(N):  # vertex
        for start, end, weight in graphs:  # grpah
            if dist[end] <= dist[start] + weight: continue

            dist[end] = dist[start] + weight
            if i == N - 1:
                return True

    return False

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())

    graphs = []
    dist = [INF for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        graphs.append((S, E, T))
        graphs.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graphs.append((S, E, -T))

    hasMinusCycle = bellman_ford()
    if hasMinusCycle:
        print('YES')
    else:
        print('NO')