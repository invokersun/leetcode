class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [([1] * n) for i in range(m)]
        for i in range(1, m):
        	for j in range(1, n):
        		f[i][j] = f[i-1][j] + f[i][j-1]
        return f[-1][-1]
print Solution().uniquePaths(3, 4)