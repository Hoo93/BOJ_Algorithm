import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graphs = dict()
for _ in range(N):
    root, left, right = sys.stdin.readline().rstrip().split()
    graphs[root] = (left, right)


def pre_order(node, result):
    result += node
    if graphs[node][0] != ".":
        result = pre_order(graphs[node][0], result)
    if graphs[node][1] != ".":
        result = pre_order(graphs[node][1], result)
    return result


def in_order(node, result):
    if graphs[node][0] != ".":
        result = in_order(graphs[node][0], result)

    result += node

    if graphs[node][1] != ".":
        result = in_order(graphs[node][1], result)
    return result


def post_order(node, result):
    if graphs[node][0] != ".":
        result = post_order(graphs[node][0], result)

    if graphs[node][1] != ".":
        result = post_order(graphs[node][1], result)

    result += node
    return result


print(pre_order("A", ""))
print(in_order("A", ""))
print(post_order("A", ""))
