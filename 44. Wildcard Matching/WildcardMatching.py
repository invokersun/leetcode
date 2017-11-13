class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        s_star = 0
        star = -1
        while i < len(s):
        	if j < len(p) and (s[i] == p[j] or p[j] == '?'):
        		i += 1
        		j += 1
        	elif j < len(p) and p[j] == '*':
        		star = j
        		j += 1
        		s_star = i
        	elif star != -1:
        		j = star + 1
        		s_star += 1
        		i = s_star
        	else:
        		return False
        while j < len(p) and p[j] == '*':
        	j += 1
        if  j == len(p):
        	return True
        	pass
        return False
x = Solution()
print x.isMatch("aa", "*")