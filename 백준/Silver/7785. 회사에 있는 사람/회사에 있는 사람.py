import sys

# f = open("practice.txt","r")
N = int(sys.stdin.readline().rstrip())
# N = int(f.readline().rstrip())
in_company = set()

for _ in range(N):
    name,enter = sys.stdin.readline().rstrip().split()
    # name,enter = f.readline().rstrip().split()
    if enter == 'enter':
        in_company.add(name)
    else:
        in_company.remove(name)

for person in sorted(in_company,reverse=True):
    print(person)
