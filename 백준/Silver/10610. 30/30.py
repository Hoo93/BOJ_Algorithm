import sys
numbers = [int(num) for num in sys.stdin.readline().rstrip()]
numbers.sort(reverse=True)

if numbers[-1] == 0:
    if sum(numbers)%3 == 0:
        print("".join(map(str,numbers)))
    else:
        print(-1)
else:
    print(-1)
