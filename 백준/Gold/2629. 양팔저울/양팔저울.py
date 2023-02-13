import sys

weights_num = int(sys.stdin.readline().rstrip())
weights = list(map(int,sys.stdin.readline().rstrip().split()))
sys.stdin.readline().rstrip()
beads = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [ set() for _ in range(weights_num)]
dp[0].add(-1*weights[0])
dp[0].add(weights[0])
dp[0].add(0)

for i in range(1,weights_num):
    for j in range(-1,2):
        for num in dp[i-1]:
            dp[i].add(num+weights[i]*j)

result = []
for bead in beads:
    if bead in dp[weights_num-1] or -1*bead in dp[weights_num-1]:
        result.append("Y")
    else:
        result.append("N")

print(" ".join(result))