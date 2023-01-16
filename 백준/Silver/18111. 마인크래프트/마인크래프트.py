import sys
import bisect

input = sys.stdin.readline
row,col,pocket = map(int,input().rstrip().split())
board = [] 
for _ in range(row):
    board += list(map(int,input().rstrip().rsplit())) 

board.sort()
maximum = max(board)

min_time = 1e9
floor = 0
for i in range(maximum+1):
    idx = bisect.bisect_right(board,i)

    pile = sum(map(lambda x : i -x ,board[:idx]))
    dig = sum(map(lambda x : x - i ,board[idx:]))
    time = pile + 2*dig

    if pocket - pile + dig  < 0:
        continue
    if time < min_time:
        min_time = time
        floor = i
    if time == min_time:
        floor = max(floor,i)
    else:
        continue

print(min_time,floor)
