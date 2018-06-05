class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        path = ["" for x in range(4)]
        self.dfs(s, 0, path, res)
        return res
    def dfs(self, s, level, path, res):
    	if not s:
    		return
    	if level == 3:
    		path[level] = s
    		if len(path[level]) <= 3 and str(int(path[level])) == path[level] and int(path[level]) <= 255:
    			res.append('.'.join(path))
    		return
    	for i in range(1,4):
    		path[level] = s[:i]
    		if str(int(path[level])) == path[level] and int(path[level]) <= 255:
    			self.dfs(s[i:], level+1, path, res)
print Solution().restoreIpAddresses("25525511135")