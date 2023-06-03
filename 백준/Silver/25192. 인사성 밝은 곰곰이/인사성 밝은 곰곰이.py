import sys

N = int(sys.stdin.readline().rstrip())
sys.stdin.readline()

result = 0
people = set()
for _ in range(N-1):
    sentence = sys.stdin.readline().rstrip()
    if sentence == "ENTER":
        result += len(people)
        people.clear()
    else:
        people.add(sentence)

result += len(people)
print(result)
