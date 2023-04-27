import sys

TC = int(sys.stdin.readline().rstrip())


def getConstTime(start):
    if len(graphs[start]) == 0:
        visited.add(start)
        path[start] = const_time[start]

        return const_time[start]

    else:
        mx = 0
        for pre in graphs[start]:
            if pre not in visited:
                visited.add(pre)
                mx = max(mx, getConstTime(pre) + const_time[start])
            else:
                mx = max(mx, path[pre] + const_time[start])

        path[start] = mx
        return mx


for _ in range(TC):
    buildings, regulation = map(int, sys.stdin.readline().rstrip().split())
    graphs = [[] for _ in range(buildings + 1)]
    visited = set()
    path = dict()
    const_time = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

    for _ in range(regulation):
        pre, post = map(int, sys.stdin.readline().rstrip().split())
        graphs[post].append(pre)

    target = int(sys.stdin.readline().rstrip())

    print(getConstTime(target))
