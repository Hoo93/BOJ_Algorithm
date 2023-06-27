import sys
import math

while True:
    word = int(sys.stdin.readline().rstrip())
    if word == -1:
        break
    
    result = set([1,])
    for i in range(2,word):
        if word % i == 0:
            result.add(i)
            result.add(word//i)
    
    if sum(result) == word:
        print(word,"="," + ".join(map(str,sorted(result))))
    else:
        print(word,"is NOT perfect.")