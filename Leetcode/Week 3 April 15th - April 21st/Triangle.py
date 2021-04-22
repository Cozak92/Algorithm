import copy

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        curLines = copy.deepcopy(triangle)
        exLine = triangle[0]

        for i in range(1,len(curLines)):

            curLines[i][0] += exLine[0]
            curLines[i][-1] += exLine[-1]
            m = len(curLines[i])

            for j in range(1,m-1):
                curLines[i][j] += min(exLine[j-1],exLine[j])
            print(curLines[i])
            exLine = curLines[i]
        
        print(min(curLines[n-1]))