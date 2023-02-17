import sys
import bisect
import copy

length = int(sys.stdin.readline().rstrip())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
LIS = []
dp = [0 for _ in range(length)]
result_length = 0
for i in range(length):
    num = num_list[i]
    idx = bisect.bisect_left(LIS,num)
    l = len(LIS)
    if idx == l:
        LIS.append(num)
        result_length += 1
    else:
        LIS[idx] = num
    
    dp[i] = idx

cnt = result_length-1
result = []
for i in range(length-1,-1,-1):
    if dp[i] == cnt:
        result.append(num_list[i])
        cnt -= 1

print(result_length)
print(" ".join(map(str,result[::-1])))