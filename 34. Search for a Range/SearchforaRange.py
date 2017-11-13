class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    	left = 0
    	right = len(nums) - 1
    	res = [-1, -1]
    	while left <= right:
    		mid = (left + right) / 2
    		if nums[mid] > target:
    			right = mid - 1
    		elif nums[mid] < target:
    			left = mid + 1
    		else:
    			res[0] = mid
    			res[1] = mid
    			i = mid - 1
    			while i>= 0 and nums[i] == target:
    				res[0] = i
    				i -= 1
    			i = mid + 1
    			while i < len(nums) and nums[i] == target:
    			 	res[1] = i
    			 	i += 1
    			break
    	return res
x = Solution()
print x.searchRange([1,7,7,8,8,9], 8)