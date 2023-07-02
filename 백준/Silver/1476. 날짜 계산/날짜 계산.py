import sys

f = sys.stdin

E,S,M = map(int,f.readline().rstrip().split())
if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0

for i in range(1,7981):
    if i%15 == E and i%28 ==S and i%19 == M:
        print(i)
        break