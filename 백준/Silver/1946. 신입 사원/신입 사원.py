import sys
import bisect

test_num = int(sys.stdin.readline().rstrip())

for _ in range(test_num):
    num = int(sys.stdin.readline().rstrip())    
    applicants = [ tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(num) ]
    applicants.sort()
    
    if num == 1:
        print(1)
        continue
    if applicants[0][1] == 1:
        print(1)
        continue

    result = [applicants[0][1]]
    
    for applicant in applicants[1:]:
        if result[-1] < applicant[1]:
            continue
        else:
            result.append(applicant[1])
        
    
    print(len(result))