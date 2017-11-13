class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        i = 0
        while i<len(nums) and i<=reach:
        	reach = max(reach, i+nums[i])
        	i += 1
        return reach>=len(nums)-1
print Solution().canJump([0])