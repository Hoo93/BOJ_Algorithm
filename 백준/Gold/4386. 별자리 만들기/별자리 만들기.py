import sys
import heapq

# f = open("practice.txt","r")

def getDist(node1,node2):
    dist = ((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)**0.5
    return round(dist,3)

N = int(sys.stdin.readline().rstrip())

nodes = []
visited = [ False for _ in range(N)]
dists = [ [ 0 for _ in range(N)] for _ in range(N)]


for _ in range(N):
    x,y = map(float,sys.stdin.readline().rstrip().split())
    nodes.append((x,y))

for i in range(N):
    for j in range(i+1,N):
        dists[i][j] = getDist(nodes[i],nodes[j])
        dists[j][i] = dists[i][j]

result = 0

hq = []

for i in range(1,N):
    heapq.heappush(hq,(dists[0][i],i))
visited[0] = True

while hq:
    dist,v = heapq.heappop(hq)
    if visited[v]:
        continue

    result += dist
    visited[v] = True

    for i in range(0,i):
        heapq.heappush(hq,(dists[v][i],i))
    
    for i in range(i+1,N):
        heapq.heappush(hq,(dists[v][i],i))
    
print(round(result,2))