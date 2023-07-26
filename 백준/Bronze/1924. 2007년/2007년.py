import sys

f = sys.stdin
# f = open("input.txt","r")
months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month,day = map(int,f.readline().rstrip().split())

result = 0
result += sum(months[:month-1])
result += day
print(days[result%7])
