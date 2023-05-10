import sys

# f = open("practice.txt", "r")
# instructions = f.readlines()
# instructions = sys.stdin.readlines()
case_num = int(sys.stdin.readline().rstrip())

st = set()
st_full = set(list(map(str, range(1, 21))))
for i in range(case_num):
    instruction = sys.stdin.readline().rstrip()

    if instruction == "all":
        st = st_full
        continue
    elif instruction == "empty":
        st.clear()
        continue

    command, num = instruction.split()

    if command == "add":
        st.add(num)
    elif command == "remove":
        if num in st:
            st.remove(num)
        else:
            continue
    elif command == "check":
        if num in st:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if num in st:
            st.remove(num)
        else:
            st.add(num)
    else:
        print("error")
