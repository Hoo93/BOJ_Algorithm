
def solution(users, emoticons):
    result = [0,0]
    
    def dfs(minDisc,maxDisc,discountedEmoticons):
        nonlocal result
        if len(discountedEmoticons) == len(emoticons):
            buyerCount = 0
            totalPrice = 0
            
            for barDiscount,barPrice in users:
                tmpPrice = 0
                for discount,price in discountedEmoticons:
                    if discount < barDiscount: continue
                    tmpPrice += price
                    
                if tmpPrice >= barPrice:
                    buyerCount += 1
                else:
                    totalPrice += tmpPrice
            
            if result[0] < buyerCount:
                result = [buyerCount, totalPrice]
            elif result[0] == buyerCount:
                result[1] = max(result[1],totalPrice)
        
            return # DFS 종료
        
        # 아직 길이가 다 차지 않은 경우
        emoticon = emoticons[len(discountedEmoticons)]
        for i in range(minDisc,maxDisc+1):
            discountedEmoticon = emoticon // 100 * (100 - i*10)
            dfs(minDisc,maxDisc,discountedEmoticons + [(10*i,discountedEmoticon)])        
    
    maxBarDiscount = 0
    minBarDiscount = 100
    
    for barDiscount, barPrice in users:
        maxBarDiscount = max(maxBarDiscount, barDiscount)
        minBarDiscount = min(minBarDiscount, barDiscount)
        
    # 십의 자리 수만 한 자리수로 가짐 range 를 편하게 쓰기 위함
    maxBarDiscount = min(4,maxBarDiscount//10 + 1)
    minBarDiscount = minBarDiscount//10 + 1
    
    # 완전탐색으로 가도 1초 안에 해결 가능함
    dfs(minBarDiscount, maxBarDiscount,[])
    
    
    return result

    
    



    
    