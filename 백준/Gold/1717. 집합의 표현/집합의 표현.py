import sys

sys.setrecursionlimit(10**6)
# f = open("practice.txt", "r")
# sentence = f.readline().rstrip()


def findRoot(node):
    if parent[node] == node:
        return node
    root = findRoot(parent[node])
    parent[node] = root
    return parent[node]


def union(node1, node2):
    node1 = findRoot(node1)
    node2 = findRoot(node2)
    if node1 == node2:
        return
    elif node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2


N, M = map(int, sys.stdin.readline().rstrip().split())
# N, M = map(int, f.readline().rstrip().split())

parent = [i for i in range(N + 1)]

for _ in range(M):
    method, a, b = map(int, sys.stdin.readline().rstrip().split())
    if method == 0:
        union(a, b)
    elif method == 1:
        if findRoot(a) == findRoot(b):
            print("YES")
        else:
            print("NO")
