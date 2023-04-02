import sys

# f = open("C:/Users/Hoo/Desktop/BaekJoon/test_case.txt", "r")
# instructions = f.readlines()
instructions = sys.stdin.readlines()

len_list = []
for i in range(len(instructions)):
    instructions[i] = instructions[i].rstrip()
    len_list.append(len(instructions[i]))

mx_len = max(len_list)
result = ""
for i in range(mx_len):
    for j in range(5):
        if i >= len_list[j]:
            continue
        result += instructions[j][i]

print(result)
