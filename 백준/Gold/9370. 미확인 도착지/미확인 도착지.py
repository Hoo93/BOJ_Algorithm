import sys
from collections import deque
import heapq

INF = 10**8

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# nums = f.readlines()


def dijsktra(graph, start, stopover):
    visited = [(INF, 0) for _ in range(vertex + 1)]
    hq = []
    heapq.heappush(hq, (0, start, 0))

    while hq:
        dist, node, flag = heapq.heappop(hq)

        if visited[node][0] < dist:
            continue
        elif visited[node][0] == dist:
            if flag:
                if visited[node][1]:
                    continue
                else:
                    visited[node] = (dist, flag)
            else:
                continue
        else:
            visited[node] = (dist, flag)

        if flag:
            for v, d in graph[node]:
                if visited[v][0] < dist + d:
                    continue
                heapq.heappush(hq, (dist + d, v, flag))
        else:
            for v, d in graph[node]:
                if visited[v][0] < dist + d:
                    continue
                if v in stopover and node in stopover:
                    heapq.heappush(hq, (dist + d, v, True))
                else:
                    heapq.heappush(hq, (dist + d, v, flag))
    return visited


test_case = int(sys.stdin.readline().rstrip())

result = []
for _ in range(test_case):

    vertex, edge, cross = map(int, sys.stdin.readline().rstrip().rstrip().split())
    start, stopover_1, stopover_2 = map(
        int, sys.stdin.readline().rstrip().rstrip().split()
    )
    graphs = [[] for _ in range(vertex + 1)]
    destination = []
    stopover = set([stopover_1, stopover_2])

    for _ in range(edge):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        graphs[a].append((b, d))
        graphs[b].append((a, d))

    for _ in range(cross):
        destination.append(int(sys.stdin.readline().rstrip()))

    visited_start = dijsktra(graphs, start, stopover)

    tmp = []
    for dest in destination:
        if visited_start[dest][1]:
            tmp.append(dest)
    tmp.sort()
    result.append(" ".join(map(str, tmp)))

for i in result:
    print(i)
