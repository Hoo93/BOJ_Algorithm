import sys

strings, brands = map(int, sys.stdin.readline().rstrip().split())
mn_set = 1000
mn_one = 1000

for _ in range(brands):
    set, one = map(int, sys.stdin.readline().rstrip().split())
    mn_set = min(mn_set, set)
    mn_one = min(mn_one, one)

if mn_one * 6 < mn_set:
    print(mn_one * strings)
else:
    if ((strings + 5) // 6) * mn_set <= strings // 6 * mn_set + (strings % 6) * mn_one:
        print(((strings + 5) // 6) * mn_set)
    else:
        print(strings // 6 * mn_set + (strings % 6) * mn_one)
