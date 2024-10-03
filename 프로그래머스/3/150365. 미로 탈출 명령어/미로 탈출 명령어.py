def solution(n, m, x, y, r, c, k):
    # d l r u
    # d:1 / u: -1
    # l:-1 /r:1
    targetRow = r - x
    targetCol = c - y
    distance = abs(targetRow) + abs(targetCol)
    rem = (k - distance) // 2
    
    if k < distance:
        return 'impossible'
    if (k - distance) % 2 == 1:
        return 'impossible'
    
    # 잉여 움직임 d l r u 순으로
    # 1. 최대한 d
    # 2. 최대한 l
    # 3. 그래도 모자르며 r l r l
    # 4. 마지막에 u
    move = [0,0,0,0]
    if r < x:
        move[3] += x - r
    if c < y:
        move[1] += y - c
    else:
        move[2] += c - y
        
    print(move)
    answer = ''
    # 최소한 d 가야하는 만큼 d를 간다.
    curY = x
    curX = y
    if r > x:
        answer += 'd'*(r-x)
        curY = r
    
    # 잉여 시작
    # 갈 수 있는 만큼 d를 간다.
    if rem and curY < n:
        if rem <= n-curY:
            answer += 'd'*rem
            move[3] += rem
            rem = 0
        else:
            answer += 'd'*(n-curY)
            rem -= (n-curY)
            move[3] += (n-curY)
    
    # 가야하는 l 만큼 간다
    answer += move[1]*'l'
    curX = y - move[1]
    
    # 갈 수 있는 만큼 l을 간다
    if rem and curX > 1:
        if rem <= curX - 1:
            answer += 'l'*rem
            move[2] += rem
            rem = 0
        else:
            answer += 'l'*(curX - 1)
            rem -= (curX - 1)
            move[2] += (curX - 1)
    
    # 그래도 rem 이 남은 경우 rlrl 왔다갔다 한다.
    if rem:
        answer += 'rl'*rem
        
    answer += move[2]*'r'
    answer += move[3]*'u'
    return answer