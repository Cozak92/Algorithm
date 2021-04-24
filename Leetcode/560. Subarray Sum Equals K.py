import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        SUM = 0
        res = 0

        counter = collections.defaultdict(int)
        counter[0] = 1

        for x in nums:

            # 구간의 합이 k가 되는 숫자가 몇번인지 구해야된다.
            # 현재까지의 합 -k가 이미 해쉬맵에 존재한다면
            # k만큼의 합이 존재했다는 뜻
            # 

            SUM += x    
            res += counter[SUM - k] 
            counter[SUM] += 1       
        return res