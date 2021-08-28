import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        global ans
        ans = sys.maxsize
        n = len(nums)
        def func(index,cnt):
            global ans
            if index == n:
                ans = min(ans,cnt)
                return
            if index > n:
                return

            for i in range(1,nums[index]+1):

                func(index+i,cnt + 1)

        func(0,0)

        return ans