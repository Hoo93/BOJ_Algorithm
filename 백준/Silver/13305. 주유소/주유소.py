import sys

input = sys.stdin.readline

node = int(input().rstrip())
distances = list(map(int,input().rstrip().split()))
prices = list(map(int,input().rstrip().split()))

result = 0

# 첫번째 node를 제외한 prices의 idx 
for i in range(1,node):
    if prices[i] > prices[i-1]:
        prices[i] = prices[i-1]

for i in range(node-1):
    result += distances[i]*prices[i]

print(result)