import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().strip().split())

x, y = 0, 0
if a != 0 and d != 0:
    a, b, c, d, e, f = d * a, d * b, d * c, a * d, a * e, a * f

    y = (c - f) // (b - e)
    x = (c - b * y) // a

elif a == 0:
    y = c // b
    x = (f - e * y) // d

else:
    y = f // e
    x = (c - b * y) // a


print(x, end=" ")
print(y, end=" ")
