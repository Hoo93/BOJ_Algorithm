import sys

coins = [25, 10, 5, 1] 
for _ in range(int(sys.stdin.readline().rstrip())):
    change = int(sys.stdin.readline().rstrip())
    result = ""
    for coin in coins:
        result += str(change//coin) + " "
        change %= coin
        
    print(result.strip())
    