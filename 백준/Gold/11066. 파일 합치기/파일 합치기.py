import sys

input = sys.stdin.readline
test_num = int(input().rstrip())
mx = 1e8
for _ in range(test_num):
    number = int(input().rstrip())
    
    num_list = [0] + list(map(int,input().rstrip().split()))
    psum = [0 for _ in range(number+1)]
    
    for i in range(1,number+1):
        psum[i] = psum[i-1] + num_list[i]

    dp = [[0 for _ in range(number+1)] for _ in range(number+1)]
    opt = [[0 for _ in range(number+1)] for _ in range(number+1)]
    
    for i in range(1,number):
        dp[i][i+1] = psum[i+1]-psum[i-1]
    
    for i in range(1,number+1):
        opt[i][i] = i
    
    for i in range(number-1,0,-1):
        for j in range(i+1,number+1):
            cost = psum[j] - psum[i-1]
            minimum = mx
            for k in range(opt[i][j-1],min(j,opt[i+1][j]+1)):
                tmp = dp[i][k]+dp[k+1][j]
                if tmp <= minimum:
                    minimum = tmp
                    opt[i][j] = k
            dp[i][j] = cost + minimum

    print(dp[1][number])