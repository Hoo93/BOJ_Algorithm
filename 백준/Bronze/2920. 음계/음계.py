import sys

num_list = list(input().rstrip().split())


if "".join(num_list) == "12345678":
    print("ascending")
elif "".join(num_list) == "87654321":
    print("descending")
else:
    print("mixed")