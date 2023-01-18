import sys

input = sys.stdin.readline

# n = int(input().rstrip())
# 앞에 0 추가하기

# eval 때릴 때 leading zero가 문제 되므로 split "+" 한 후에 int로 계산 
expression ="0"+ input().rstrip()
expressions = expression.split("-")
result = 0

def make_int(sentence:str):
    tmp = 0
    for num in sentence.split("+"):
        tmp += int(num)
    return tmp

result = make_int(expressions[0])

for i in expressions[1:]:
    result -= make_int(i)

print(result)