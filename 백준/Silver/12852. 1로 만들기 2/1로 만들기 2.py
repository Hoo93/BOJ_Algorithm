import sys

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
INF = 10**6

instructions = int(sys.stdin.readline().rstrip())

dp = [INF for _ in range(instructions + 1)]
action = [0 for _ in range(instructions + 1)]

dp[1] = 0
action[1] = -1
for i in range(2, instructions + 1):
    if i % 3 == 0:
        if dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            action[i] = 3
    if i % 2 == 0:
        if dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            action[i] = 2

    if dp[i - 1] + 1 < dp[i]:
        dp[i] = dp[i - 1] + 1
        action[i] = -1

print(dp[instructions])
while instructions >= 1:
    print(instructions, end=" ")
    if action[instructions] != -1:
        instructions //= action[instructions]
    else:
        instructions -= 1
