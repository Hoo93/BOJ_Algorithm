def subDate(dateA,dateB):
    return (dateA[0] - dateB[0])*12*28 + (dateA[1] - dateB[1])*28 + (dateA[2] - dateB[2])
        
def addMonth(date,month):
    return [date[0],date[1]+month,date[2]]

def solution(today, terms, privacies):
    answer = []
    
    todayDate = list(map(int,today.split('.')))
    
    expiredMonth = dict()
    
    for term in terms:
        contract,month = term.split()
        
        expiredMonth[contract] = int(month)
    
    for idx,privacy in enumerate(privacies):
        signedDate,contract = privacy.split()
        
        signedDate = list(map(int,signedDate.split('.')))
        
        expirationDate = addMonth(signedDate,expiredMonth[contract])
        
        differaceExpirationDateByToday = subDate(expirationDate,todayDate)
        
        if differaceExpirationDateByToday <= 0:
            answer.append(idx+1)

    return answer