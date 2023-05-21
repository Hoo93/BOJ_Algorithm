import sys

sys.setrecursionlimit(10**6)
# f = open("practice.txt", "r")
# sentence = f.readline().rstrip()


def findRoot(node):
    if roots[node] == node:
        return node
    root = findRoot(roots[node])
    roots[node] = root
    return roots[node]


def union(node1, node2):
    node1 = findRoot(node1)
    node2 = findRoot(node2)
    if node1 == node2:
        return
    elif node1 < node2:
        roots[node2] = node1
    else:
        roots[node1] = node2


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
# N, M = map(int, f.readline().rstrip().split())

roots = [i for i in range(N + 1)]

for i in range(N):
    nlt = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if nlt[j]:
            union(i, j)

path = list(map(int, sys.stdin.readline().rstrip().split()))

result = "YES"
for i in range(M - 1):
    if findRoot(path[i] - 1) == findRoot(path[i + 1] - 1):
        continue
    else:
        result = "NO"
        break

print(result)
