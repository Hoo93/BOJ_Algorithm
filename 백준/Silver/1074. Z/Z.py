import sys

sys.setrecursionlimit(10**6)

N, r, c = map(int, sys.stdin.readline().rstrip().split())
dp = dict()
dp[(0, 0)] = 0
dp[(0, 1)] = 1
dp[(1, 0)] = 2
dp[(1, 1)] = 3


def getPath(r, c, N):
    if N == 1:
        return dp[(r, c)]
    if r < 2 ** (N - 1):
        if c < 2 ** (N - 1):
            return getPath(r, c, N - 1)
        else:
            return getPath(r, c - (2 ** (N - 1)), N - 1) + 2 ** (2 * N - 2)
    else:
        if c < 2 ** (N - 1):
            return getPath(r - (2 ** (N - 1)), c, N - 1) + 2 ** (2 * N - 1)
        else:
            return (
                getPath(r - (2 ** (N - 1)), c - (2 ** (N - 1)), N - 1)
                + 2 ** (2 * N - 2) * 3
            )


print(getPath(r, c, N))
