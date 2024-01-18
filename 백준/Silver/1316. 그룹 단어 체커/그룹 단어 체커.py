import sys

def isGroupWord(word: str) -> bool:
    existLetter = set()

    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            continue
        else:
            if word[i] in existLetter:
                return False
            else:
                existLetter.add(word[i])

    if word[-1] in existLetter:
        return False
    return True

result = 0
for _ in range(int(sys.stdin.readline().strip())):
    result += isGroupWord(sys.stdin.readline().strip())

print(result)