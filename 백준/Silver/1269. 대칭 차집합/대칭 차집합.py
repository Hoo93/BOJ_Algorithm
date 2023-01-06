import sys
input = sys.stdin.readline
n,l = map(int,input().rstrip().rsplit())
set_a = set()
set_b = set()

set_a.update(map(int,input().rstrip().rsplit()))
set_b.update(map(int,input().rstrip().rsplit()))

print(len(set_a)+len(set_b)-2*len(set_b.intersection(set_a)))