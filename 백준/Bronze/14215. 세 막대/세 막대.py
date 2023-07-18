import sys

f = sys.stdin
# f = open("input.txt","r")

sentences = sorted(map(int,f.readline().rstrip().split()))

if sentences[2] >= sentences[1] + sentences[0]:
    print(2*(sentences[1] + sentences[0]) - 1)
else:
    print(sum(sentences))