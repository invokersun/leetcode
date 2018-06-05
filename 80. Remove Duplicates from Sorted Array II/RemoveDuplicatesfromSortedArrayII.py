class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
        	return 0
        idx = 0
        count = 0
        for i in xrange(0, len(nums)):
        	if i > 0 and nums[i]==nums[i-1]:
        		count += 1
        		if count >= 3:
        			continue
        	else:
        		count = 1
        	nums[idx] = nums[i]
        	idx += 1
        return idx
print Solution().removeDuplicates([3])