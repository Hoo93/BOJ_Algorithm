import sys

N = int(sys.stdin.readline().rstrip())

sentence = sys.stdin.readline().rstrip()
length = len(sentence)
for _ in range(N-1):
    n_sentence = sys.stdin.readline().rstrip()
    tmp = ""
    for i in range(length):
        if sentence[i] == n_sentence[i]:
            tmp += sentence[i]
        else:
            tmp += '?'
    sentence = tmp
print(sentence)