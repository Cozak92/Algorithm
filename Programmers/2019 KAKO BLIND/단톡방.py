def solution(record):
    findDict = {}
    order = []
    answer = []
    for r in record:
        r = list(r.split(" "))

        if r[0] == "Enter" or r[0] == "Change":
            findDict[r[1]] = r[2]

        order.append((r[0], r[1]))
    
    for o in order:
        if o[0] == "Enter":
            answer.append(findDict[o[1]] + "님이 들어왔습니다.")
        elif o[0] == "Leave":
            answer.append(findDict[o[1]] + "님이 나갔습니다.")

            
            
            

    
        
        
        
        
    
    
    return answer