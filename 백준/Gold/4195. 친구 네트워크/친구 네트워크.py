import sys

sys.setrecursionlimit(10**6)
# f = open("practice.txt", "r")


def find(name: str):
    if name == people[name]:
        return name

    root = find(people[name])
    people[name] = root
    return people[name]


def union(name1: str, name2: str):
    name1, name2 = find(name1), find(name2)

    if name1 == name2:
        return True
    elif name1 < name2:
        people[name2] = name1
        nFreinds[name1] += nFreinds.pop(name2)
        return True

    else:
        people[name1] = name2
        nFreinds[name2] += nFreinds.pop(name1)
        return False


TC = int(sys.stdin.readline().rstrip())

for _ in range(TC):
    people = dict()
    nameSet = set()
    nFreinds = dict()
    F = int(sys.stdin.readline().rstrip())
    for _ in range(F):
        name1, name2 = sys.stdin.readline().rstrip().split()

        if name1 not in nameSet:
            nameSet.add(name1)
            people[name1] = name1
            nFreinds[name1] = 1

        if name2 not in nameSet:
            nameSet.add(name2)
            people[name2] = name2
            nFreinds[name2] = 1

        if union(name1, name2):
            print(nFreinds[find(name1)])
        else:
            print(nFreinds[find(name2)])
