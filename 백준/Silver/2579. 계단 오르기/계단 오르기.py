import sys
input = sys.stdin.readline

n = int(input().strip())
num_list = [0]

for _ in range(n):
    num_list.append(int(input().strip()))

if n == 1:
    print(num_list[1])
elif n == 2:
    print(num_list[1]+num_list[2])
else:
    dp_table = [[0,0] for _ in range(n+1)]
    
    dp_table[1][0] = num_list[1]
    dp_table[2][0] = num_list[2]
    dp_table[2][1] = num_list[1] + num_list[2]
    
    for i in range(3,n+1):
        dp_table[i][0] = max(dp_table[i-2][0]+num_list[i], dp_table[i-2][1]+num_list[i])
        dp_table[i][1] = dp_table[i-1][0]+num_list[i]
    
    print(max(dp_table[n][1],dp_table[n][0]))

