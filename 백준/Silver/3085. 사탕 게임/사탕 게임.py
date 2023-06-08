import sys
import copy

size = int(sys.stdin.readline().rstrip())
board = [ sys.stdin.readline().rstrip() for _ in range(size) ]

# f = open("practice.txt","r")
# size = int(f.readline().rstrip())
# board = [ f.readline().rstrip() for _ in range(size) ]

def findMaxLen(board):
    result = 0 
    
    for i in range(size):
        stack = [board[i][0]]
        for j in range(1,size):
            if not stack or stack[-1] == board[i][j]:
                stack.append(board[i][j])
            else:
                result = max(result,len(stack))
                stack = [board[i][j]]
        result = max(result,len(stack))

    for j in range(size):
        stack = [board[0][j]]
        for i in range(1,size):
            if not stack or stack[-1] == board[i][j]:
                stack.append(board[i][j])
            else:
                result = max(result,len(stack))
                stack = [board[i][j]]
        result = max(result,len(stack))
    
    return result

def changeBoard(n_board,node_1,node_2):
    # 행이 같은 경우
    board = copy.deepcopy(n_board)
    if node_1[0] == node_2[0]:
        x1,x2 = min(node_1[1],node_2[1]),max(node_1[1],node_2[1])
        y = node_1[0]
        sentence = list(board[y])
        sentence[x1],sentence[x2] = sentence[x2],sentence[x1]
        board[y] = "".join(sentence)
    else:
        y1,y2 = min(node_1[0],node_2[0]),max(node_1[0],node_2[0])
        x = node_1[1]

        tmp = board[y1][x]

        board[y1] = board[y1][:x] + board[y2][x] + board[y1][x+1:]
        board[y2] = board[y2][:x] + tmp + board[y2][x+1:]
    
    return board

def getMaxLen():
    if findMaxLen(board) == size:
        return size
    else:
        result = 0

        for i in range(size):
            for j in range(size-1):
                if board[i][j] != board[i][j+1]:
                    result = max(result,findMaxLen(changeBoard(board,(i,j),(i,j+1))))
                    if result == size:
                        return size
                else:
                    continue
                
        for j in range(size):
            for i in range(size-1):
                if board[i][j] != board[i+1][j]:
                    result = max(result,findMaxLen(changeBoard(board,(i,j),(i+1,j))))
                    if result == size:
                        return size
                else:
                    continue
                
        return result
    
print(getMaxLen())
