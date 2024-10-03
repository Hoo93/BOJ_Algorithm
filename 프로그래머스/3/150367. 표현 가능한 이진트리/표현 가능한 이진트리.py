# 숫자를 입력 받아 길이 2^n -1 의 binary string 으로 변환한다.
def convertBinary(number):
    result = bin(number)[2:]
    
    n = 1
    targetLength = len(result)
    while True:
        if 2**n - 1 < targetLength:
            n += 1
        else:
            break
    
    result = result.zfill(2**n-1)
    return result
    

# 길이 2^n -1 의 이진수를 binary tree 로 표현 가능한지 검사
def isBinaryTree(binary):
    if len(binary) == 1:
        return 1
    
    center = len(binary)//2
    
    if binary[center] == '0':
        if int(binary) == 0:
            return 1
        return 0
    
    return isBinaryTree(binary[:center]) and isBinaryTree(binary[center+1:])
    

def solution(numbers):
    
    answer = []
    for number in numbers:
        answer.append(isBinaryTree(convertBinary(number)))
    
    # 짤리는 경우가 있는지 검사하는 dfs 함수
    return answer