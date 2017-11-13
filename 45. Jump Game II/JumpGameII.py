class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, steps = 0, 0, 0
        while end < len(nums) - 1:
        	steps += 1
        	farthest = end
        	for i in xrange(start, end + 1):
        		if nums[i] + i > farthest:
        			farthest = nums[i] + i
        	start = end + 1
        	end = farthest
        return steps
x = Solution()
print x.jump([2, 3, 1, 1, 4])