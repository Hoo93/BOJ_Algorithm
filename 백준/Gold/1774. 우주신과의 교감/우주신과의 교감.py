import sys
import heapq

# f = open("practice.txt","r")

def find(node):
    if roots[node] == node:
        return node
    
    root = find(roots[node])
    roots[node] = root
    return roots[node]

def union(node1,node2):
    node1,node2 = find(node1),find(node2)

    if node1 == node2:
        return
    elif node1 < node2:
        roots[node2] = node1
    else:
        roots[node1] = node2
    
    return

def getDist(node1,node2):
    dist = ((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)**0.5
    return dist

# N,M = map(int,f.readline().rstrip().split())
N,M = map(int,sys.stdin.readline().rstrip().split())

nodes = [(-1,-1)]
roots = [ i for i in range(N+1)]
hq = []

for _ in range(N):
    # x,y = map(int,f.readline().rstrip().split())
    x,y = map(int,sys.stdin.readline().rstrip().split())
    nodes.append((x,y))

for i in range(1,N+1):
    for j in range(i+1,N+1):
        heapq.heappush(hq,(getDist(nodes[i],nodes[j]),i,j))

for i in range(M):
    # n1,n2 = map(int,f.readline().rstrip().split())
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    union(n1,n2)

result = 0

while hq:
    cost,n1,n2 = heapq.heappop(hq)
    if find(n1) == find(n2):
        continue
    else:
        result += cost
        union(n1,n2)

print(f"{result:.2f}")