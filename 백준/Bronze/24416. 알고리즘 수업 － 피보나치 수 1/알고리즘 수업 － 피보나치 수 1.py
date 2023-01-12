import sys
n = int(sys.stdin.readline().strip())
count = 1
def fib(n):
    global count
    if n == 1 or n == 2:
        return 1  # 코드1
    else:
        count+=1
        return (fib(n - 1) + fib(n - 2))

fib(n)
print(count,n-2)
