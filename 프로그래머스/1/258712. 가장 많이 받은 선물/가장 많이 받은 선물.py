def solution(friends, gifts):
    answer = 0
    idxDict = {}
    
    
    for idx,friend in enumerate(friends):
        idxDict[friend] = idx
        
    # [준 선물 수, 받은 선물 수]
    records = [[ [0,0] for _ in range(50)] for _ in range(50)]
    
    for gift in gifts:
        giver,receiver = gift.split()
        giverIdx = idxDict[giver]
        receiverIdx = idxDict[receiver]
        
        records[giverIdx][receiverIdx][1] += 1
        records[receiverIdx][giverIdx][0] += 1
    
    
    giftScore = [0 for _ in range(50)]
    for idx,record in enumerate(records):
        giveSum = 0
        receiveSum = 0
        
        for g,r in record:
            giveSum += g
            receiveSum += r
            
        giftScore[idx] = giveSum - receiveSum
        
    giftResult = [ [ 0 for _ in range(50)] for _ in range(50)]
    
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            # 준 선물이 많은 경우
            if records[i][j][0] < records[i][j][1]:
                giftResult[i][j] += 1
            elif records[i][j][0] > records[i][j][1]:
                giftResult[j][i] += 1
            else:
                if giftScore[i] < giftScore[j]:
                    giftResult[i][j] += 1
                elif giftScore[i] > giftScore[j]:
                    giftResult[j][i] += 1
    
    mx = 0
    for result in giftResult:
        mx = max(sum(result),mx)
        
    for i in range(len(friends)):
        print(records[i][:len(friends)])
    
    print(giftScore[:len(friends)])
    
    for result in giftResult[:len(friends)]:
        print(result[:len(friends)])
    
    return mx