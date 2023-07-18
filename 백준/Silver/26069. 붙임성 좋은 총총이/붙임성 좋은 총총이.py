import sys

f = sys.stdin
# f = open("input.txt","r")

N = int(f.readline().rstrip())
visited = set(["ChongChong"])
for _ in range(N):
    name1,name2 = f.readline().rstrip().split()
    if name1 in visited or name2 in visited:
        visited.add(name2)
        visited.add(name1)

print(len(visited))