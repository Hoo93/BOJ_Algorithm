import sys
from collections import deque

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
INF = 10**6

# instructions = int(sys.stdin.readline().rstrip())

str_one = sys.stdin.readline().rstrip()
str_two = sys.stdin.readline().rstrip()
row = len(str_one)
col = len(str_two)

dp = [[(0, "") for _ in range(col + 1)] for _ in range(row + 1)]

# queue = deque([(0, 0)])

# while queue:
#     r, c = queue.popleft()
#     if r >= row or c >= col:
#         continue
#     if str_one[r] == str_two[c]:
#         dp[r + 1][c + 1] = (dp[r][c][0] + 1, dp[r][c][1] + str_one[r])
#         queue.append((r + 1, c + 1))
#     else:
#         if dp[r][c][0] > dp[r + 1][c][0]:
#             dp[r + 1][c] = dp[r][c]
#         queue.append((r + 1, c))
#         if dp[r][c][0] > dp[r][c + 1][0]:
#             dp[r][c + 1] = dp[r][c]
#         queue.append((r, c + 1))


# if dp[row][col - 1][0] == 0 and dp[row - 1][col][0] == 0:
#     print(0)
# else:
#     if dp[row - 1][col][0] >= dp[row][col - 1][0]:
#         print(dp[row - 1][col][0])
#         print(dp[row - 1][col][1])
#     else:
#         print(dp[row][col - 1][0])
#         print(dp[row][col - 1][1])

for r in range(row):
    for c in range(col):
        if str_one[r] == str_two[c]:
            dp[r + 1][c + 1] = (dp[r][c][0] + 1, dp[r][c][1] + str_one[r])
        else:
            if dp[r + 1][c][0] >= dp[r][c + 1][0]:
                dp[r + 1][c + 1] = dp[r + 1][c]
            else:
                dp[r + 1][c + 1] = dp[r][c + 1]

if dp[row][col][0] == 0:
    print(0)
else:
    print(dp[row][col][0])
    print(dp[row][col][1])
