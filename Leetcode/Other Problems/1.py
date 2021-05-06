import sys

INF = sys.maxsize

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        
        counts = [ [0,0] for _ in range(len(strs))]
        SUM = [ [0,0] for __ in range(len(strs)+1) ]
        
        print(strs)
        
        for i in range(len(strs)):
   
            counts[i][0] = strs[i].count("0")
            counts[i][1] = strs[i].count("1")
            
        start, end = 0, 1
        MAX = -INF
        
        print(counts)
        print(SUM)
        
        for i in range(1,(len(strs)+1)):
            
            SUM[i][0] = SUM[i-1][0] + counts[i-1][0]
            SUM[i][1] = SUM[i-1][1] + counts[i-1][1]
            
            print(SUM[i][0],SUM[i][1])
            
        print()
                     
        
        while start < len(strs)-1:
            
            cntZero = SUM[end][0] - SUM[start][0]
            cntOne = SUM[end][1] - SUM[start][1]
            print(cntZero,cntOne)
            
            if cntZero > m or cntOne > n:
                start += 1
            else:
                MAX = max(MAX,end-start)
                #print(start,end)
                
                if end != n+1:
                    end += 1
                else:
                    start += 1
        return MAX
                
            
            
            
            
            
        
        