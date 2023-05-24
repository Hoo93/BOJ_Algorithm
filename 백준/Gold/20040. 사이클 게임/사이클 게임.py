import sys

sys.setrecursionlimit(10**6)
# f = open("practice.txt", "r")
roots = {}


def find(node: int):
    if roots[node] == node:
        return node

    root = find(roots[node])
    roots[node] = root
    return roots[node]


def union(node1: int, node2: int):
    if node1 < node2:
        roots[node2] = node1
    else:
        roots[node1] = node2


instructions = sys.stdin.readlines()
N, M = map(int, instructions[0].rstrip().split())
result = 0
for i in range(1, M + 1):
    node1, node2 = map(int, instructions[i].rstrip().split())
    if node1 not in roots.keys():
        roots[node1] = node1

    if node2 not in roots.keys():
        roots[node2] = node2

    rNode1, rNode2 = find(node1), find(node2)

    if rNode1 == rNode2:
        result = i
        break

    else:
        union(rNode1, rNode2)

print(result)
