import sys

input = sys.stdin.readline
n = int(input().rstrip())
board = [ list(map(int,input().rstrip().split())) for _ in range(n)] 
result = [0,0,0]
def check_paper(x:int,y:int,size:int):
    tmp = board[x][y]
    for i in range(size):
        for j in range(size):
            if not board[x+i][y+j] == tmp:
                check_paper(x,y,size//3)
                check_paper(x+size//3,y,size//3)
                check_paper(x+2*size//3,y,size//3)
                check_paper(x,y+size//3,size//3)
                check_paper(x+size//3,y+size//3,size//3)
                check_paper(x+2*size//3,y+size//3,size//3)
                check_paper(x,y+2*size//3,size//3)
                check_paper(x+size//3,y+2*size//3,size//3)
                check_paper(x+2*size//3,y+2*size//3,size//3)
                return
    result[tmp+1] += 1
    
check_paper(0,0,n)
for i in result:
    print(i)