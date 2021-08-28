# def check(orders, order,isChecked):
    
#     orderCnt = 1
    
#     for otherOrder in orders:
#         if not isChecked[otherOrder]:
#             dp = [[0 for _ in range(len(order)+1)] for __ in range(len(otherOrder)+1)]
            
#             for x in range(1, (len(otherOrder)+1)):
#                 for y in range(1, (len(order)+1)):
                    
#                     if otherOrder[x-1] == order[y-1]:
#                         dp[x][y] = dp[x-1][y-1] +1

#                     else:
#                         dp[x][y] = max(dp[x-1][y], dp[x][y-1])
#             #print(*dp)
            
#             if dp[x][y] >= len(order):
#                 #print(otherOrder,order)
#                 orderCnt += 1
                           
#     return orderCnt
                        
                    
            
            
        
        

# def solution(orders, course):
#     answer = []
#     isChecked = {}
#     maxNum = [ 0 for _ in range(11)]
#     maxOrder = [ " " for _ in range(11)]
    
#     print(orders)
#     for order in orders:
#         isChecked[order] = 0
    
#     for num in course:
        
#         for order in orders:
            
#             if len(order) == num:
#                 isChecked[order] = 1
#                 orderCounts = check(orders,order,isChecked)
#                 print(orderCounts)

#                 if maxNum[num] < orderCounts:
#                     maxNum[num] = orderCounts
#                     maxOrder[num] = order
#                     print(maxNum,maxOrder)
#                 elif maxNum[num] == orderCounts:
#                     answer.append(order)

   



#     for num in course:
#         answer.append(maxOrder[num])

#     answer.sort()
                
                
#     return answer


from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k): #현재 주문에서 k개 만큼뽑아서 조합
                res = ''.join(sorted(li))
                candidates.append(res) #뽑은것을 배열에다가 넣어줌
            #print(candidates)
        sorted_candidates = Counter(candidates).most_common() # !!!중요!!! Counter함수를 사용해서 각각 몇개있는지 대신 세줌... 거의 치트키 수준
        #print(sorted_candidates)
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]] #최대값과 같은거 가져오기

        
        #어떤식으로 코딩했는지 보고 배우자
    return sorted(answer)


order = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(order,course))