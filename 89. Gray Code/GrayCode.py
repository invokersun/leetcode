class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = [0]
        for i in range(n):
        	results += [x + pow(2, i) for x in reversed(results)]
        return results
print Solution().grayCode(3)