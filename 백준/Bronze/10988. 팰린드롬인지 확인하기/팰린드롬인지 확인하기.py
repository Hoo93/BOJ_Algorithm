import sys
string = sys.stdin.readline().rstrip()
print(int(string == string[::-1]))