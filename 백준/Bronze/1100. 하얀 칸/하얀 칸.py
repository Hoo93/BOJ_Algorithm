import sys

result = 0

for i in range(8):
    board = sys.stdin.readline().rstrip()
    start = i%2
    for j in range(start,8,2):
        if board[j] != ".":
            result += 1

print(result)