# import copy
# res = 0
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
#         global res
#         row = len(obstacleGrid[0])
#         column = len(obstacleGrid)
#         dp =[ [-1 for _in range(row)] for __ in range(column) ]
#         dx = [0,1]
#         dy = [1,0]
#         res = 0
#         if obstacleGrid[0][0] == 1:
#             return 0
#         isVisited = [[False for _ in range(row)] for __ in range(column) ]
#         isVisited[0][0] = True
#         def dfs(x,y,isVisited):
#             #rint("x,y = " ,x,y)
#             global res
#             copiedVisit = copy.deepcopy(isVisited)

#             if x == column -1 and y == row - 1 and obstacleGrid[x][y] != 1:
#                 return 1
#                 #print("res =",res)
#             if dp[x][y] != -1:
#                 return dp[x][y]

#             for i in range(2):
                
#                 #print(dx[i],dy[i])

#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 #print("nx,ny = " ,nx,ny)

#                 if 0 <= ny < row and 0 <= nx < column and obstacleGrid[nx][ny] != 1:
#                     if not copiedVisit[nx][ny]:
#                         copiedVisit[nx][ny] = True
#                         dp[x][y] = dfs(nx,ny,copiedVisit)

#             return dp[x][y]
#         dfs(0,0,isVisited)
#         return dp[0][0]
# import copy
# res = 0

# def solution(obstacleGrid):
#     row = len(obstacleGrid[0])
#     column = len(obstacleGrid)
#     dx = [0,1]
#     dy = [1,0]
    
#     isVisited = [[False for _ in range(row)] for __ in range(column) ]
#     isVisited[0][0] = True
#     def dfs(x,y,isVisited):
#         print("x,y = " ,x,y)
#         global res
#         copiedVisit = copy.deepcopy(isVisited)

#         if x == column -1 and y == row - 1 and obstacleGrid[x][y] != 1:
#             res += 1
#             print("res =",res)

#         for i in range(2):
            
#             print(dx[i],dy[i])

#             nx = x + dx[i]
#             ny = y + dy[i]
#             print("nx,ny = " ,nx,ny)

#             if 0 <= ny < row and 0 <= nx < column and obstacleGrid[nx][ny] != 1:
#                 if not copiedVisit[nx][ny]:
#                     copiedVisit[nx][ny] = True
#                     dfs(nx,ny,copiedVisit)

#         return 0
#     dfs(0,0,isVisited)
#     print(res)
#     return res

# solution([[0,1],[0,0]])

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]