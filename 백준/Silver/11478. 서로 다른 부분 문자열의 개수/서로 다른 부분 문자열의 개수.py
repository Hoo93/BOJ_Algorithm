import sys
input = sys.stdin.readline
word = input().rstrip()
partial_word = set()

for i in range(1,len(word)+1):
    for j in range(len(word)-i+1):
        partial_word.add(word[j:j+i])

print(len(partial_word))