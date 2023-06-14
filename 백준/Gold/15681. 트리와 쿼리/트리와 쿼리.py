import sys
sys.setrecursionlimit(10**6)

# f = open("practice.txt","r")
# N,R,Q = map(int,f.readline().rstrip().split())
N,R,Q = map(int,sys.stdin.readline().rstrip().split())

graphs = [[] for _ in range(N+1)]
parents = [ -1 for _ in range(N+1)]
subTreeNum = [0 for _ in range(N+1)]

for _ in range(N-1):
    # n1,n2 = map(int,f.readline().rstrip().split())
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    graphs[n1].append(n2)
    graphs[n2].append(n1)

def makeTree(node,parent):
    parents[node] = parent
    for v in graphs[node]:
        if v == parent:
            continue
        else:
            makeTree(v,node)

def getSubtreeNum(node):
    cnt = 1
    for v in graphs[node]:
        if v == parents[node]:
            continue
        cnt += getSubtreeNum(v)
    
    subTreeNum[node] = cnt
    return cnt
    

makeTree(R,-1)
getSubtreeNum(R)

for i in range(Q):
    q = int(sys.stdin.readline().rstrip())
    print(subTreeNum[q])
