import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        SUM = 0
        res = 0

        counter = collections.defaultdict(int)
        counter[0] = 1

        for x in nums:

            SUM += x    
            res += counter[SUM - k] 
            counter[SUM] += 1       
        return res