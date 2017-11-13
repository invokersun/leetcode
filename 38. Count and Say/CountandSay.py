class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        while n > 1:
        	res = self.countStr(res)
        	n -= 1
        return res
    def countStr(self, s):
    	count = 0
    	res = ""
    	tmp = s[0]
    	for i in range(len(s)):
    		if s[i] == tmp:
    			count += 1
    		else:
    			res += str(count) + tmp
    			tmp = s[i]
    			count = 1
    	res += str(count) + tmp
    	return res
x = Solution()
print x.countAndSay(20)