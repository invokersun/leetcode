class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
    #     res = [[]]
    #     tmp = []
    #     self.dfs(res, tmp, n, k, 1)
    #     return res
    # def dfs(self, res, tmp, n, k, m):
    # 	if k == 0:
    # 		res.append(tmp)
    # 		return
    # 	for i in range(m, n+1):
    # 		tmp.append(i)
    # 		self.dfs(res, tmp, n, k-1, i+1)
    # 		tmp.pop(len(tmp)-1)
        stack = []
        res = []
        l, x = 0, 1
        while True:
            if l == k:
                res.append(stack[:])
            if l == k or n-x+1 < k-l:
                if not stack:
                    return res
                x = stack.pop() + 1
                l -= 1
            else:
                stack.append(x)
                x += 1
                l += 1
print Solution().combine(4, 2)
# class Solution(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         res = []
#         self.dfs(res, 0, n, k, [])
#         return res
#     def dfs(self, res, i, n, k, temp):
#         if k == 0 :
#             res.append(temp)
#             return
#         for j in range(i+1, n+1):
#             self.dfs(res, j, n, k-1, temp+[j])