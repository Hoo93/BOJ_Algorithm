import sys

f = sys.stdin
# f = open("input.txt","r")

stack = []

vowel = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
while True:
    sentence = f.readline().rstrip()
    result = 0
    if sentence == "#":
        break
    for char in sentence:
        if char in vowel:
            result += 1
    print(result)
