from collections import deque

def solution(priorities, location):

    
    
    priorities = deque(priorities)
    table = deque()
    for i in range(len(priorities)):
        table.append([i,priorities[i]])

    order = 0
    while table:
        MAX = -1
        index, value = table.popleft()
        print(index,value)
        for t in table:
            MAX = max(MAX,t[1])
        if value >= MAX:
            order += 1
            if index == location:
                return order
        else:
            table.append([index,value])

solution([1, 1, 9, 1, 1, 1],0)
            


