class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        r, c, m = len(s1), len(s2), len(s3)
        if r+c != m:
        	return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
        	x, y = stack.pop()
        	if x+y == m:
        		return True
        	if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
        		stack.append((x+1, y))
        		visited.add((x+1, y))
        	if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
        		stack.append((x, y+1))
        		visited.add((x, y+1))
        return False
print Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
print Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc')