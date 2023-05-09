import sys

sys.setrecursionlimit(10**6)

# f = open("practice.txt", "r")
# instructions = f.readlines()
instructions = sys.stdin.readlines()


def getDist(point, crime) -> int:
    return abs(point[0] - crime[0]) + abs(point[1] - crime[1])


size = int(instructions[0].rstrip())
case_num = int(instructions[1].rstrip())
dp = [[-1 for _ in range(case_num + 1)] for _ in range(case_num + 1)]
path = [[-1 for _ in range(case_num + 1)] for _ in range(case_num + 1)]


crimes = [[0, 0]]
for instruction in instructions[2:]:
    crimes.append(tuple(map(int, instruction.rstrip().split())))

# dp[1][0] = getDist(police1, crimes[1])
# dp[1][2] = dp[1][0] + getDist(police2, crimes[2])
# dp[0][1] = getDist(police2, crimes[1])
# dp[2][1] = dp[0][1] + getDist(police1, crimes[2])

# for i in range(2, case_num + 1):
#     dp[i][0] = dp[i - 1][0] + getDist(crimes[i - 1], crimes[i])
#     dp[0][i] = dp[0][i - 1] + getDist(crimes[i - 1], crimes[i])

# for i in range(3, case_num + 1):
#     dp[i][1] = dp[i - 1][1] + getDist(crimes[i - 1], crimes[i])
#     dp[1][i] = dp[1][i - 1] + getDist(crimes[i - 1], crimes[i])


# 이렇게 하면 0 일 때 police1,2 의 위치가 다르게 나와서 해결 안됨
def solve(police1, police2):
    if dp[police1][police2] != -1:
        return dp[police1][police2]

    if police1 == case_num or police2 == case_num:
        return 0

    next = max(police1, police2) + 1

    if police1 == 0:
        d1 = getDist(crimes[next], (1, 1))
    else:
        d1 = getDist(crimes[next], (crimes[police1]))

    if police2 == 0:
        d2 = getDist(crimes[next], (size, size))
    else:
        d2 = getDist(crimes[next], crimes[police2])

    c1 = solve(next, police2) + d1
    c2 = solve(police1, next) + d2

    # if c1 < c2:
    #     dp[]
    dp[police1][police2] = min(c1, c2)
    return dp[police1][police2]


def printPath(police1, police2):
    if max(police1, police2) == case_num:
        return

    next = max(police1, police2) + 1

    if police1 == 0:
        d1 = getDist(crimes[next], (1, 1))
    else:
        d1 = getDist(crimes[next], (crimes[police1]))

    if police2 == 0:
        d2 = getDist(crimes[next], (size, size))
    else:
        d2 = getDist(crimes[next], crimes[police2])

    c1 = solve(next, police2) + d1
    c2 = solve(police1, next) + d2

    if c1 < c2:
        print(1)
        printPath(next, police2)
    else:
        print(2)
        printPath(police1, next)


print(solve(0, 0))
printPath(0, 0)
