class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = m = -10000000000000000000
        for n in nums:
        	m = max(n, m+n)
        	res = max(m, res)
        return res
print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])