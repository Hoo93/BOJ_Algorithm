import sys

index = int(sys.stdin.readline().rstrip().split()[0])

word_list = sys.stdin.readlines()
checks = set(word_list[:index])
words = word_list[index:]

count= 0

for word in words:
    if word in checks:
        count+=1
        
print(count)