import sys

input = sys.stdin.readline

input()
word = input().rstrip()
dic = {}
answer = 0
hash = 1
for i in range(97,123):
    dic[chr(i)] = i-96

for i in range(len(word)):
    answer += (dic[word[i]]*hash)%1234567891
    hash *= 31

print(answer)