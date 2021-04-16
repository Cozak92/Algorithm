class Solution:
    def minOperations(self, n: int) -> int:
        SUM = 0
        
        for i in range(n):
            SUM += (i*2) + 1
        
        median = SUM //n
        
        print(counts = set(abs(median-(i*2+1)) for i in range(n)))