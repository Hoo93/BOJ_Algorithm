import sys
from collections import deque

# f = open("practice.txt", "r")
# sentence = f.readline().rstrip()

N = int(sys.stdin.readline().rstrip())


def getCoins(num):
    if num == 3 or num <= 1:
        return -1

    result = 0

    result += num // 5
    num %= 5
    if num % 2 == 1:
        num += 5
        result -= 1

    result += num // 2

    return result


print(getCoins(N))
