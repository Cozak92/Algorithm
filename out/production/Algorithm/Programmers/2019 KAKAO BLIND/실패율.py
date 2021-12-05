def solution(N, stages):
    players = len(stages)
    failRate = {}
    stages.sort()
    
    totalPlayers = players
    for i in range(1,N+1):
        if totalPlayers <= 0:
            failRate[i] = 0
            continue
        curPlayers = stages.count(i)
        failRate[i] = curPlayers/totalPlayers
        totalPlayers -= curPlayers
        
    
    failRate = sorted(failRate, key=lambda x : failRate[x],reverse = True)
    print(failRate)
        
            
  
    return failRate
    

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

solution(N, stages)