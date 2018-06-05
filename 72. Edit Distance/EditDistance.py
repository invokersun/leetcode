class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        ans = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            ans[i][n] = m - i
        for i in range(n + 1):
            ans[m][i] = n - i
        m -= 1;n -= 1
        while m >= 0:
            t = n
            while t >= 0:
                if word1[m] == word2[t]:
                    ans[m][t] = ans[m + 1][t + 1]
                else:
                    ans[m][t] = min(ans[m][t+1],ans[m+1][t],ans[m+1][t+1]) + 1
                t -= 1
            m -= 1
        return ans[0][0]
print Solution().minDistance('abc', 'abdc')