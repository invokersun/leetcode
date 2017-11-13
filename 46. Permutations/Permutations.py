class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], nums)
        return res
    def dfs(self, res, numList, theNums):
    	if len(theNums) == 0:
    		res.append(list(numList))
    	for i in xrange(len(theNums)):
    		numList.append(theNums[i])
    		self.dfs(res, numList, theNums[:i] + theNums[i+1:])
    		numList.pop()
x = Solution()
print x.permute([1, 2, 3, 4, 5])