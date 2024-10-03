def solution(cap, n, deliveries, pickups):
    answer = -1
    
    dIndex = n - 1
    pIndex = n - 1
    
    result = 0
    
    while dIndex >= 0 or pIndex >= 0:
        while dIndex >= 0:
            if not deliveries[dIndex]:
                dIndex -= 1
                continue
            break
        
        while pIndex >= 0:
            if not pickups[pIndex]:
                pIndex -= 1
                continue
            break
        
        result += max(pIndex, dIndex) + 1
        
        space = cap
        while space and dIndex >= 0:
            if not deliveries[dIndex]:
                dIndex -= 1
                continue
            
            if deliveries[dIndex] <= space:
                space -= deliveries[dIndex]
                deliveries[dIndex] = 0
            else:
                deliveries[dIndex] -= space
                space = 0
        
        space = cap
        while space and pIndex >= 0:
            if not pickups[pIndex]:
                pIndex -= 1
                continue
            
            if pickups[pIndex] <= space:
                space -= pickups[pIndex]
                pickups[pIndex] = 0
            else:
                pickups[pIndex] -= space
                space = 0
                
    
    return 2*result