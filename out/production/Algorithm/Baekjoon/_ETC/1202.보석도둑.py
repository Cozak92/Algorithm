import sys
input = sys.stdin.readline
import heapq

# def findingBags(bagIndex,gemIndex):
#     if bagIndex > k or gemIndex > n:
#         return 0

#     if dp[gemIndex][bagIndex] != -1:
#         return dp[gemIndex][bagIndex]
#     print(bagIndex,gemIndex)
#     if bags[bagIndex] >= gems[gemIndex - 1][0]:

#         dp[gemIndex][bagIndex] = max(findingBags(bagIndex + 1, gemIndex +1) + gems[gemIndex-1][1],findingBags(bagIndex + 1, gemIndex))
#     else:
#         dp[gemIndex][bagIndex] = findingBags(bagIndex+ 1,gemIndex)

#     return dp[gemIndex][bagIndex]





n, k = list(map(int,list(input().split())))
maxWeight, maxValue = -1, -1
gems = []
bags = []

q = []



# dp =[[-1 for _ in range(k+1)] for __ in range(n+1)]


for i in range(n):
    weight, value = list(map(int,list(input().split())))
    gems.append([weight,value])
    #maxWeight = max(maxWeight,gem[i][0])
    #maxValue = max(maxValue,gem[i][1])


gems = sorted(gems)
#print(gems)
#print(gems)


for i in range(k):
    bags.append(int(input()))
    #print(bags)

bags = sorted(bags)

answer = 0 
index = 0
for bag in bags:
  
    while index < n:
        weight, value = gems[index]

        if weight <= bag:  
            heapq.heappush(q,-gems[index][1])
            index += 1
        else: break

    # for gem in gems:
    #     weight, value = gem

    #     if weight <= bag:
    #         heapq.heappush(q,-value)
    #     else: break

        #print("index",index)
    #print(q)
    #print(bag)


    if q:
        answer += -heapq.heappop(q)
        
    #print(q)
        

    

print(answer)

