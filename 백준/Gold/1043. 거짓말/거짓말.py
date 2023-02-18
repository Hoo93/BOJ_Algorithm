import sys
sys.setrecursionlimit(10**7)

n,m = map(int,sys.stdin.readline().rstrip().split())
truth = sys.stdin.readline().rstrip()
parties = [list(map(int,sys.stdin.readline().rstrip().split()))[1:] for _ in range(m)]

if truth == "0":
    print(m)
else:
    truth = list(map(int,truth.split()))
    tmp = set(truth[1:])
    tmp_two = set()
    dp = [ True for _ in range(m)]
    
    while len(tmp)>0:
        for i in range(m):
            for person in parties[i]:
                if person not in tmp:
                    continue
                if dp[i]:
                    dp[i] = False
                    tmp_two = tmp_two.union(set(parties[i]))
                    break
        tmp = tmp_two.difference(tmp)
        tmp_two = set()
    
    print(sum(dp))