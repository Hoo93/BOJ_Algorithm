import sys

# f = open("pratice.txt","r")
f = sys.stdin

for _ in range(3):
    N = int(f.readline().rstrip())
    result = 0
    for _ in range(N):
        result += int(f.readline().rstrip())
    
    if result > 0:
        print("+")
    elif result == 0:
        print("0")
    else:
        print("-")