class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        totalNums = nums1 + nums2
        totalNums = totalNums.sort()
        print(totalNums)
        N = len(totalNums)
        answer = 0
        
        if N % 2 == 0:
            answer = (totalNums[N//2] + totalNums[N//2 - 1]) / 2 
        else:
            answer = totalNums[N//2]
        return answer