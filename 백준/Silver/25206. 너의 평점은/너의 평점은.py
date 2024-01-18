import sys

num_sum = 0
score = 0

g = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}
for _ in range(20):
    _,num,grade = sys.stdin.readline().strip().split()
    if grade == 'P':
        continue
    else:
        score += float(num)*g[grade]
        num_sum += float(num)

print(round(score/num_sum,5))