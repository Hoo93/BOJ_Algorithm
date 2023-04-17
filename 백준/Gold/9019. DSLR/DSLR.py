import sys
from collections import deque
import heapq

for _ in range(int(input())):
    A, B = map(int, input().split())
    queue = deque()
    queue.append((A, ""))
    visit = [False] * 10000

    while queue:
        num, path = queue.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break

        n_num = (2 * num) % 10000
        if not visit[n_num]:
            queue.append((n_num, path + "D"))
            visit[n_num] = True
        n_num = (num - 1) % 10000
        if not visit[n_num]:
            queue.append((n_num, path + "S"))
            visit[n_num] = True
        n_num = (10 * num + (num // 1000)) % 10000
        if not visit[n_num]:
            queue.append((n_num, path + "L"))
            visit[n_num] = True

        n_num = (num // 10 + (num % 10) * 1000) % 10000
        if not visit[n_num]:
            queue.append((n_num, path + "R"))
            visit[n_num] = True
