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

    
    # optimization array / 초기값 설정
    for i in range(1,number+1):
        opt[i][i] = i
    
    for start in range(number-1,0,-1):
        for end in range(start+1,number+1):
            cost = psum[end] - psum[start-1]
            minimum = mx
            # Knuth Optimization 을 사용해 mid 의 범위를 축소 시킴 !!!!!
            # mid의 값은 end 보다는 작아야 하므로 min()을 사용해줌
            for mid in range(opt[start][end-1],min(end,opt[start+1][end]+1)):
                tmp = dp[start][mid]+dp[mid+1][end]

                # 최단 경로의 값과 그 때의 중간 경로 지점을 opt에 저장
                if tmp <= minimum:
                    minimum = tmp
                    opt[start][end] = mid
            dp[start][end] = cost + minimum

    print(dp[1][number])