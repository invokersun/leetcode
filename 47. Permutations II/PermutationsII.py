class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(res, [], None, nums)
        return res
    def dfs(self, res, theList, pre, nums):
        if len(nums) == 0:
            res.append(list(theList))
        pre = None
        for i in xrange(len(nums)):
            if nums[i] == pre:
                continue
            theList.append(nums[i])
            self.dfs(res, theList, nums[i], nums[:i] + nums[i+1:])
            theList.pop()
            pre = nums[i]
x = Solution()
print x.permuteUnique([1, 1, 2])