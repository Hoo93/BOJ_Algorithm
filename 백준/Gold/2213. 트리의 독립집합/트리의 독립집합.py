import sys

def makeTree(node,parent):
    parents[node] = parent

    for v in graphs[node]:
        if v == parent:
            continue
        else:
            makeTree(v,node)

def getMaxWeigh(node,selected):
    if dp[node][selected] > -1:
        return dp[node][selected]
    
    # if len(graphs[node]) == 1:
    #     if selected:
    #         dp[node][1] = vertex_weigh[node]
    #         return dp[node][1]
    #     else:
    #         dp[node][0] = 0
    #         return dp[node][0]
    
    if selected:
        tmp = vertex_weigh[node]
        for v in graphs[node]:
            if v == parents[node]:
                continue
            tmp += getMaxWeigh(v,False)
        
        dp[node][1] = max(tmp,dp[node][1])
        return dp[node][1]
    
    else:
        tmp = 0
        for v in graphs[node]:
            if v == parents[node]:
                continue
            tmp += max(getMaxWeigh(v,True),getMaxWeigh(v,False))
        
        dp[node][0] = max(tmp,dp[node][0])
        return dp[node][0]

def getPath(node,selected):
    if selected:
        path = [node]
        
        for v in graphs[node]:
            if v == parents[node]:
                continue
            else:
                path += getPath(v,False)
        
        return path

    else:
        path = []
        for v in graphs[node]:
            if v == parents[node]:
                continue
            if dp[v][1] >= dp[v][0]:
                path += getPath(v,True)
            else:
                path += getPath(v,False)
        
        return path


sentences = sys.stdin.readlines()
# f = open("practice.txt","r")
# sentences = f.readlines()
vertex = int(sentences[0].rstrip())
vertex_weigh = [0] + list(map(int,sentences[1].rstrip().split()))
parents = [0 for _ in range(vertex+1)]
graphs = list([] for _ in range(vertex+1))

for sentence in sentences[2:]:
    n1,n2 = map(int,sentence.rstrip().split())
    graphs[n1].append(n2)
    graphs[n2].append(n1)

# N번 노드를 포함한 서브트리의 가중치의 최대값
dp = [ [-1,-1] for _ in range(vertex+1)]
path = [ 0 for _ in range(vertex+1)]

makeTree(vertex//2,-1)
getMaxWeigh(vertex//2,True)
getMaxWeigh(vertex//2,False)

if dp[vertex//2][1] >= dp[vertex//2][0]:
    print(dp[vertex//2][1])
    print(" ".join(map(str,sorted(getPath(vertex//2,True)))))
else:
    print(dp[vertex//2][0])
    print(" ".join(map(str,sorted(getPath(vertex//2,False)))))
