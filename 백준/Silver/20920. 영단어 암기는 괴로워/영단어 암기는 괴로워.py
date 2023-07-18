import sys

f = sys.stdin
# f = open("input.txt","r")

memory = set()
countWord = dict()

N, M = map(int,f.readline().rstrip().split())

for _ in range(N):
    word = f.readline().rstrip()
    if len(word) < M:
        continue
    if word in memory:
        countWord[word] += 1
    else:
        memory.add(word)
        countWord[word] = 1

result = []
for word in countWord.keys():
    result.append((countWord[word],word))

result.sort(key = lambda x:x[1])
result.sort(key = lambda x:len(x[1]),reverse=True)
result.sort(key = lambda x:x[0],reverse=True)

for word in result:
    print(word[1])

