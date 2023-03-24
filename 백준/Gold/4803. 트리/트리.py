import sys
from collections import deque

sys.setrecursionlimit(10**8)

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# nums = f.readlines()
nums = sys.stdin.readlines()
for i in range(len(nums)):
    nums[i] = list(map(int, nums[i].rstrip().split()))

idx = 0
test_case = []
while idx < len(nums) and nums[idx][0] != 0:
    v, e = nums[idx]
    test_case.append(nums[idx : idx + e + 1])
    idx += e + 1


def countTree(case):
    def isTree(node):

        que = deque()
        que.append((node, 0))
        flag = True

        while que:
            v, v_before = que.popleft()
            if visited[v]:
                flag = False
                continue
            visited[v] = True

            for n_v in graphs[v]:
                if n_v == v_before:
                    continue
                if visited[n_v]:
                    flag = False
                    continue
                que.append((n_v, v))

        return flag

    result = 0
    v, e = case[0]

    visited = [False for _ in range(v + 1)]
    graphs = [[] for _ in range(v + 1)]

    for start, end in case[1:]:
        graphs[start].append(end)
        graphs[end].append(start)

    for i in range(1, v + 1):
        if not visited[i]:
            if isTree(i):
                result += 1

    return result


for i in range(len(test_case)):

    result = countTree(test_case[i])
    print(f"Case {i+1}:", end=" ")
    if result == 0:
        print("No trees.")
    elif result == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {result} trees.")
