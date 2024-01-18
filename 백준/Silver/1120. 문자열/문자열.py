import sys
input = sys.stdin.readline

longer ,shorter = input().split()

if len(shorter) >= len(longer):
    longer,shorter = shorter,longer

result = 50
tmp = 0

for i in range(len(longer) - len(shorter)+1):
    for j in range(len(shorter)):
        if (shorter[j] != longer[i+j]):
            tmp += 1
    result = min(result,tmp)
    tmp = 0

print(result)