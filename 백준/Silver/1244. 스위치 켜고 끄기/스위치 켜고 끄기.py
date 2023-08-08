import sys

f = sys.stdin

switchNum = int(f.readline().rstrip())
switchStatus = [0] + list(map(int, f.readline().rstrip().split()))

people = int(f.readline().rstrip())

for _ in range(people):
    isMale, switchLocation = map(int, f.readline().rstrip().split())

    if isMale % 2:
        for i in range(switchLocation, switchNum + 1, switchLocation):
            switchStatus[i] = abs(switchStatus[i] - 1)
    else:
        length = 0
        while True:
            if (
                length < switchLocation <= switchNum - length
                and switchStatus[switchLocation - length]
                == switchStatus[switchLocation + length]
            ):
                length += 1
            else:
                break

        switchStatus[switchLocation] = abs(switchStatus[switchLocation] - 1)
        for i in range(length):
            switchStatus[switchLocation - i] = abs(switchStatus[switchLocation - i] - 1)
            switchStatus[switchLocation + i] = abs(switchStatus[switchLocation + i] - 1)
        # print("length : ", length)
cnt = 0
for i in range(1, switchNum + 1):
    print(switchStatus[i], end=" ")
    cnt += 1
    if cnt == 20:
        cnt = 0
        print()
