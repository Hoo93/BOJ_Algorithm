import sys

f = sys.stdin
# f = open("input.txt","r")

word = f.readline().rstrip()

size = (len(word)-1) // 10

for i in range(size):
    print(word[10*i:10*(i+1)])
print(word[size*10:])