import sys

input = sys.stdin.readline
test_num = int(input().rstrip())
for _ in range(test_num):
    number = int(input().rstrip())
    
    num_list = [0] + list(map(int,input().rstrip().split()))
    psum = [[0 for _ in range(number+1)] for _ in range(number+1)]
    
    for i in range(1,number+1):
        tmp = 0
        for j in range(i,number+1):
            tmp += num_list[j]
            psum[i][j] = tmp
    
    dp = [[0 for _ in range(number+1)] for _ in range(number+1)]
    
    for i in range(1,number):
        dp[i][i+1] = psum[1][i+1]-psum[1][i-1]
    
    for i in range(2,number):
        for j in range(1,number+1-i):
            minimum = dp[j][j] + dp[j+1][j+i]
            for k in range(j+1,j+i):
                tmp = dp[j][k]+dp[k+1][j+i]
                if tmp < minimum:
                    minimum = tmp
            dp[j][j+i] = psum[j][j+i] + minimum
    
    print(dp[1][number])