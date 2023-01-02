import sys

a = int(sys.stdin.readline().rstrip())

def digit_sum(num:int)->int:
    result = num
    while num>0:
        result += num%10
        num //= 10
    return result

def search_maker(num:int):
    if num <= 18:
        for i in range(1,num):
            if digit_sum(i) == num:
                return i
    else:
        for i in range(num- 9*len(str(num)),num):
            if digit_sum(i) == num:
                return i
    return 0

print(search_maker(a))