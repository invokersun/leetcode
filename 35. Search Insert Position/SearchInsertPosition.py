class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
        	mid = (left + right) / 2
        	if target == nums[mid]:
        		return mid
        	elif target > nums[mid]:
        		left = mid + 1
        	else: 
        		right = mid - 1
        return left
x=Solution()
print x.searchInsert([1,3,5,7], 9)