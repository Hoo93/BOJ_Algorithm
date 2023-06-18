import sys
    
#counterClockWise
def CCW(x1,y1,x2,y2,x3,y3):
    if (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1) > 0:
        return 1
    elif (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1) < 0:
        return -1
    else:
        return 0

def isCrossed(line1,line2):
    x1,y1,x2,y2 = line1
    x3,y3,x4,y4 = line2
    tmp1 = CCW(x1,y1,x2,y2,x3,y3)
    tmp2 = CCW(x1,y1,x2,y2,x4,y4)
    tmp3 = CCW(x3,y3,x4,y4,x1,y1)
    tmp4 = CCW(x3,y3,x4,y4,x2,y2)

    if tmp1*tmp2 > 0:
        return False
    
    elif tmp1*tmp2 == 0:
        if tmp3*tmp4 > 0:
            return False

        elif tmp3*tmp4 == 0:
            if tmp1 != 0 or tmp2 != 0:
                return True
            
            if ((x1 <= x4) and (x3 <= x2)) and ((y1 <= y4) and (y3 <= y2)):
                return True
            else:
                return False
            
        else:
            return True
    
    else:
        if tmp3*tmp4 > 0:
            return False
        else:
            return True

def find(node):
    if roots[node] == node:
        return node
    
    roots[node] = find(roots[node])
    return roots[node]

def union(node1,node2):
    node1,node2 = find(node1),find(node2)

    if node1 < node2:
        roots[node2] = node1
    else:
        roots[node1] = node2

# f = open("practice.txt","r")
# N = int(f.readline().rstrip())

N = int(sys.stdin.readline().rstrip())
lines = [(0,0,0,0)]
roots = [i for i in range(N+1)]
cnt = [ 0 for _ in range(N+1) ]
groups = set()

for _ in range(N):
    # x1,y1,x2,y2 = map(int,f.readline().rstrip().split())
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    
    if x1 < x2:
        lines.append((x1,y1,x2,y2))
    
    elif x1 == x2:
        if y1 <= y2:
            lines.append((x1,y1,x2,y2))
        else:
            lines.append((x2,y2,x1,y1))
    
    else:
        lines.append((x2,y2,x1,y1))


for i in range(1,N+1):
    for j in range(1,N+1):
        n1,n2 = find(i),find(j)
        if n1 == n2:
            continue
        else:
            if isCrossed(lines[i],lines[j]):
                union(i,j)
            else:
                continue

for i in range(1,N+1): 
    roots[i] = find(roots[i])

for i in range(1,N+1):
    cnt[roots[i]] += 1
    groups.add(roots[i])

print(len(groups))
print(max(cnt[1:N+1])) 


# for i in range(2,N+1):
#     print(lines[1],"*",lines[i],":",isCrossed(lines[1],lines[i]))
