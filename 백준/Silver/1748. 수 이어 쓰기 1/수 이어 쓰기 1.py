N = input().rstrip()

length = len(N)
result = 0 

for i in range(1,length):
    result += i * 9 * 10**(i-1)

result += length * (int(N) - 10**(length-1)+1)

print(result)