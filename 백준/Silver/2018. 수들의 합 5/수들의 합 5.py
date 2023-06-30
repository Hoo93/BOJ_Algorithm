import sys

# f = open("practice.txt","r")
f = sys.stdin

N = int(f.readline().rstrip())

result = 0
left = 0
right = 1
tmp = 1

while right <= N and left <= N:
    if tmp == N:
        result += 1
        left += 1
        tmp -= left
    elif tmp > N:
        left += 1
        tmp -= left
    else:
        right += 1
        tmp += right
    

print(result)


