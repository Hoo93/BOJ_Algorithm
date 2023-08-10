import sys

f = sys.stdin
# f = open("input.txt", "r")

word = f.readline().rstrip()
alpha = [0 for _ in range(26)]

for char in word:
    alpha[ord(char) - 65] += 1

impossible = 0
result = ""
center = ""
for i in range(26):
    if alpha[i] == 0:
        continue
    elif alpha[i] % 2 == 1:
        impossible += 1
        result += chr(i + 65) * (alpha[i] // 2)
        center = chr(i + 65)
    else:
        result += chr(i + 65) * (alpha[i] // 2)

    if impossible >= 2:
        print("I'm Sorry Hansoo")
        break

if impossible < 2:
    print(result + center + result[::-1])
