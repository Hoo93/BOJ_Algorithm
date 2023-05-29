import sys

V,E = map(int,sys.stdin.readline().rstrip().split())

graphs = []
roots = [ i for i in range(V+1)]

def find(node):
    if roots[node] == node:
        return node
    
    root = find(roots[node])
    roots[node] = root
    return roots[node]


def union(node1,node2):
    rNode1,rNode2 = find(node1),find(node2)
    
    if rNode1 == rNode2:
        return 
    elif rNode1 < rNode2:
        roots[rNode2] = rNode1
    else:
        roots[rNode1] = rNode2
    
    return 

    

for _ in range(E):
    s,e,d = map(int,sys.stdin.readline().rstrip().split())
    graphs.append((d,s,e))

graphs.sort()

MST = 0

for d,s,e in graphs:
    if find(s) == find(e):
        continue
    else:
        MST += d
        union(s,e)


print(MST)