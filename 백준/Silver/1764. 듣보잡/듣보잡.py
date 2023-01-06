import sys
input = sys.stdin.readline
n,l = map(int,input().rstrip().rsplit())
check_listen = set()
check_see = set()

for i in range(n):
    check_listen.add(input().strip())
for i in range(l):
    check_see.add(input().strip())

answer = sorted(check_listen.intersection(check_see))
print(len(answer))
for word in answer:
    print(word)