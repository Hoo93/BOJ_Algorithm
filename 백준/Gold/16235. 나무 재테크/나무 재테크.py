import sys
from collections import deque
import heapq

instructions = sys.stdin.readlines()

N, M, K = map(int, instructions[0].rstrip().split())
farm = [[5 for _ in range(N + 2)] for _ in range(N + 2)]
tree = [[[] for _ in range(N + 2)] for _ in range(N + 2)]
machine = (
    [[0 for _ in range(N + 2)]]
    + [
        [0] + list(map(int, instructions[i].rstrip().split())) + [0]
        for i in range(1, N + 1)
    ]
    + [[0 for _ in range(N + 2)]]
)

for i in range(N + 1, N + M + 1):
    r, c, age = map(int, instructions[i].rstrip().split())
    tree[r][c].append(age)

# N, M, K = map(int, sys.stdin.readline().rstrip().split())
# farm = [[[5, []] for _ in range(N + 2)] for _ in range(N + 2)]
# machine = (
#     [[0 for _ in range(N + 2)]]
#     + [
#         [0] + list(map(int, sys.stdin.readline().rstrip().split())) + [0]
#         for i in range(N)
#     ]
#     + [[0 for _ in range(N + 2)]]
# )

# for i in range(M):
#     r, c, age = map(int, sys.stdin.readline().rstrip().split())
#     heapq.heappush(tree[r][c], age)


def spring_summer():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            idx = len(tree[r][c])
            length = len(tree[r][c])
            tree[r][c].sort()
            for i in range(length):
                if tree[r][c][i] <= farm[r][c]:
                    farm[r][c] -= tree[r][c][i]
                    tree[r][c][i] += 1
                else:
                    idx = i
                    break

            for _ in range(length - idx):
                farm[r][c] += tree[r][c].pop() // 2


delta = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]


def autumn():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            for i in range(len(tree[r][c])):
                if tree[r][c][i] % 5 == 0:
                    for dr, dc in delta:
                        tree[r + dr][c + dc].append(1)


def winter():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            farm[r][c] += machine[r][c]


def one_year():
    spring_summer()
    autumn()
    winter()


for _ in range(K):
    one_year()

result = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        result += len(tree[r][c])

print(result)
