import sys
sys.setrecursionlimit(10**6)
# def makeTree(node,parent):
#     parents[node] = parent

#     for v in graphs[node]:
#         if v == parent:
#             continue
#         makeTree(v,node)

def getMinAdopter(node,parent,selected):
    if dp[node][selected] != N:
        return dp[node][selected]
    
    cnt = selected
    
    if selected:
        for v in graphs[node]:
            if v == parent:
                continue
            cnt += min(getMinAdopter(v,node,True),getMinAdopter(v,node,False))
        
    else:
        for v in graphs[node]:
            if v == parent:
                continue
            cnt += getMinAdopter(v,node,True)
    
    dp[node][selected] = cnt
    return dp[node][selected]


# f = open("practice.txt","r")
# N = int(f.readline().rstrip())

N = int(sys.stdin.readline().rstrip())

graphs = [[] for _ in range(N+1)]
dp = [[N,N] for _ in range(N+1)]
parents = [-1 for _ in range(N+1)]

for _ in range(N-1):
    # n1,n2 = map(int,f.readline().rstrip().split())
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    graphs[n1].append(n2)
    graphs[n2].append(n1)

getMinAdopter(1,-1,True)
getMinAdopter(1,-1,False)

print(min(dp[1]))
