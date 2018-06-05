class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
        	if i == 0 or nums[i] != nums[i-1]:
        		length = len(res)
        	for j in range(len(res)-length, len(res)):
        		res.append(res[j] + [nums[i]])
        return res
print Solution().subsetsWithDup([1,2,2])