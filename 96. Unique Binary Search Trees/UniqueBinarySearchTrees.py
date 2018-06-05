class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = [0 for x in range(n+1)]
        m[0] = m[1] = 1
        for i in xrange(2, n+1):
        	for j in xrange(1, i+1):
        		m[i] += m[j-1] * m[i-j]
       	return m[n]
print Solution().numTrees(4)