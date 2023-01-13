import sys

input = sys.stdin.readline

number = int(input().strip())
number_list =[0]+ [ int(input().strip()) for _ in range(number) ]

dp = [[0,0,0] for _ in range(number+1)]

if number >= 2:
    dp[1][1] = number_list[1]
    dp[2][0] = number_list[1]
    dp[2][1] = number_list[2]
    dp[2][2] = number_list[2] + number_list[1]
    
    for i in range(3,number+1):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
        dp[i][1] = dp[i-1][0] + number_list[i]
        dp[i][2] = dp[i-1][1] + number_list[i]

    # for i in range(len(dp)):
    #     print(i,":",dp[i])

    
    print(max(max(dp[number]),max(dp[number-1])))
else:
    print(number_list[1])
