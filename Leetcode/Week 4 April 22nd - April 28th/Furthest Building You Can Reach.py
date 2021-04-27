# def dfs(index,heights,bricks,ladders,dp):
    
#     #print(index, bricks,ladders)
    
#     if index >= len(heights) - 1:
#         return 0
#     if dp[index][ladders] != -1:
#          return dp[index][ladders]
    

#     curBuilding = heights[index]
#     nextBuilding = heights[index + 1]
    
    
#     if curBuilding < nextBuilding:
        
#         gap = nextBuilding - curBuilding

#         if gap <= bricks and ladders > 0:
            
#             dp[index][ladders] = max(dfs(index+1,heights,bricks - gap, ladders,dp),
#                                 dfs(index+1,heights,bricks,ladders - 1,dp)) + 1
#         elif gap > bricks and ladders > 0:
#             dp[index][ladders] = dfs(index+1,heights,bricks,ladders - 1,dp) + 1
#         elif gap <= bricks and ladders == 0:
#             #print(index,bricks,ladders)
#             dp[index][ladders] = dfs(index+1,heights,bricks - gap, ladders,dp) + 1
            
#         else: return 0
#     else:
        
#         dp[index][ladders] = dfs(index+1,heights,bricks,ladders,dp) + 1
        
    
    

#     return dp[index][ladders]


#####################DFS 아니여따...########

    



import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        pq = [] # 힙큐정의

        for i in range(len(heights) - 1):
            gap = heights[i + 1] - heights[i]
            if gap > 0 : #gap이 0보다 크다는 뜻은 뒤 빌딩이 더 크다는 뜻
                heapq.heappush(pq,gap) # 사다리를 태우는 숫자
            if len(pq) > ladders: #사다리의 한계를 넘었으면
                bricks -= heapq.heappop(pq) # 가장 작은 갭만큼 벽돌에서 빼준다.
            if bricks < 0: # 벽돌이 0이 됐다면 더이상 진행못함
                return i
        return len(heights) - 1
        