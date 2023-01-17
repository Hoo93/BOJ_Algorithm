import sys

input = sys.stdin.readline

word = input().rstrip()
q = int(input().rstrip())

dp = [[0 for _ in range(26)] for _ in range(len(word)+1)]
dp[1][ord(word[0])-97] = 1

for i in range(1,len(word)):
    for j in range(26):
        dp[i+1][j] = dp[i][j]
    idx = ord(word[i])-97
    dp[i+1][idx] += 1

for _ in range(q):
    alpha,start,end = input().rstrip().split()
    idx = ord(alpha)-97
    print(dp[int(end)+1][idx] - dp[int(start)][idx])