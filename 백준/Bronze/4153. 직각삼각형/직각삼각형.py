import sys
input = sys.stdin.readline
answer = ""
triangle = input().strip()

while triangle != "0 0 0":
    num_list = sorted(map(int,triangle.split()))

    if num_list[2]**2 == num_list[1]**2 + num_list[0]**2:
        answer += "right\n"
    else:
        answer += "wrong\n"
    
    triangle = input().strip()

print(answer)