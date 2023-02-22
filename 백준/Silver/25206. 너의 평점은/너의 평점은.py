import sys

pass_and_fail = set(['P','F'])
result = 0
total = 0
dic = dict()

for grade,point in [('F',0),('D0',1.0),('D+',1.5),('C0',2.0),('C+',2.5),('B0',3.0),('B+',3.5),('A0',4.0),('A+',4.5)]:
    dic[grade] = point

for _ in range(20):

    a,b,c = sys.stdin.readline().rstrip().split()
    if c == 'P':
        continue
    
    result += dic[c]*float(b)
    total += float(b)

print(round(result/total,5))