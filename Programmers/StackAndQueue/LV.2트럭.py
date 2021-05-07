from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    bridge.append((truck_weights[0],0))
    curTime = 0
    index = 1
    while(bridge):
        curTime += 1
        if sum(bridge) < weight:
            bridge.append((truck_weights[index],curTime))
            index += 1
        else:
            if bridge[0][1] >= bridge_length:
                bridge.popleft()
            
        
    return curTime

print(solution(2,10,[7,4,5,6]))