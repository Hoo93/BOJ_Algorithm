import sys

f = sys.stdin

N = int(f.readline().rstrip())

def recurStar(size):
    if size == 3:
        return ["  *  "," * * ","*****"]
    size //= 2
    star = recurStar(size)
    new_star = []
    for i in range(size):
        new_star.append(" "*(size) + star[i] +" "*(size))
    
    for i in range(size):
        new_star.append(star[i] + " " + star[i])
    
    return new_star

for i in recurStar(N):
    print(i)
