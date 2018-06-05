class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        for x in nums:
        	with_x = []
        	for s in res:
        		with_x.append(s + [x])
        	res = res + with_x
        return res
print Solution().subsets([1, 2, 3])