alpha = [ 0 for _ in range(26)]

for char in input().rstrip():
    alpha[ord(char)-97] += 1
    
for i in alpha:
    print(i, end=" ")