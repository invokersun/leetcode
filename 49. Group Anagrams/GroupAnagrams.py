class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d, ans = {}, []
        for i in strs:
        	sortstr = ''.join(sorted(i))
        	if sortstr in d:
        		d[sortstr] += [i]
        	else:
        		d[sortstr] = [i]
        for i in d:
        	tmp = d[i]
        	tmp.sort()
        	ans += [tmp]
        return ans
print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])