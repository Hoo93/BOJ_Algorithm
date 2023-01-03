import sys

sys.stdin.readline().rstrip()
compare_list = set(map(int,sys.stdin.readline().rstrip().rsplit()))
sys.stdin.readline().rstrip()
num_list = list(map(int,sys.stdin.readline().rstrip().rsplit()))

for i in num_list:
    print(1 if i in compare_list else 0 ,end=" ")
        