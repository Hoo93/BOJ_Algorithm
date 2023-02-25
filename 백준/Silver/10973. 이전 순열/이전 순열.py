import sys
import bisect
size = int(sys.stdin.readline().rstrip())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))

answer = []
if size == 1:
    print(-1)
else:
    idx = size - 1 
    for i in range(size-1,0,-1):
        if num_list[i] > num_list[i-1]:
            continue
        else:
            idx = i - 1
            break

    if idx == size -1:
        print(-1)
    else:
        answer = num_list[:idx]
        tmp = num_list[idx]
        tmp_list = num_list[idx+1:]
        i = bisect.bisect_left(tmp_list,tmp) - 1
        answer += [tmp_list[i]]
        tmp_list.remove(tmp_list[i])
        tmp_list.append(tmp)
        answer += sorted(tmp_list,reverse=True)
        print(" ".join(map(str,answer)))