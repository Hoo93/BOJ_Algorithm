import sys

letters = sys.stdin.readline().rstrip() + ' '
result = len(letters) -1

def isKroatia(idx: int) -> bool:
    if letters[idx] == 'c':
        if letters[idx+1] == '=' or letters[idx+1] == '-':
            return True
    elif letters[idx] == 'd':
        if letters[idx+1] == '-':
            return True
        elif letters[idx+1] == 'z' and letters[idx+2] == '=':
            return True
    elif letters[idx] == 'l' and letters[idx+1] == 'j':
        return True
    elif letters[idx] == 'n' and letters[idx+1] == 'j':
        return True
    elif letters[idx] == 's' and letters[idx+1] == '=':
        return True
    elif letters[idx] == 'z' and letters[idx+1] == '=':
        return True
    return False

for i in range(len(letters) - 1):
    result -= isKroatia(i)

print(result)