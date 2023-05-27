import sys

sys.setrecursionlimit(10**6)



def find(node):
    if roots[node] == node:
        return node

    root = find(roots[node])
    roots[node] = root
    return roots[node]


def union(node):
    pass


TC = int(sys.stdin.readline().rstrip())

for _ in range(TC):
    N, M = map(int, sys.stdin.readline().rstrip().split())

    roots = [i for i in range(N + 1)]

    for _ in range(M):
        s, e = map(int, sys.stdin.readline().rstrip().split())

    print(N - 1)
