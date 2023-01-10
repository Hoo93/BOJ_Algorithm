import sys
case_num = int(sys.stdin.readline())

for _ in range(case_num): 
    closet = dict()
    answer = 1
    num = int(sys.stdin.readline())

    if num == 0:
        print(0)
        continue

    for i in range(num):
        clothes = sys.stdin.readline().rstrip().rsplit()
        if clothes[1] in closet:
            closet[clothes[1]] += 1
        else:
            closet.update({clothes[1]:1})

    for cloth in closet.keys():
        answer *= closet[cloth]+1
    print(answer - 1)
    