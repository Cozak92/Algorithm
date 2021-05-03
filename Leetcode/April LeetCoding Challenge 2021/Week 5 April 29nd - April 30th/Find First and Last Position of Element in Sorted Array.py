class Solution:

	def searchRange(self, nums: List[int], target: int) -> List[int]:

		def findFirstAndSecond(nums, lo, hi, target):
			if lo > hi: return [-1, -1]

			mid = (lo+hi)//2

			if nums[mid] < target:
				return findFirstAndSecond(nums, mid+1, hi, target)
			elif nums[mid] > target:
				return findFirstAndSecond(nums, lo, mid-1, target)
			else:
				first = findFirstAndSecond(nums, lo, mid-1, target)[0]
				last = findFirstAndSecond(nums, mid+1, hi, target)[1]
				if first == -1: first = mid
				if last == -1: last = mid

				return [first, last]

		return findFirstAndSecond(nums, 0, len(nums)-1, target)