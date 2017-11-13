class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.re = []
        self.backtracking(candidates, target, 0, [])
        return Solution.re
    def backtracking(self, candidates, target, start, val):
        if target == 0 and val not in Solution.re:
            Solution.re.append(val)
        else:
            for i in range(start,len(candidates)):
                if target < candidates[i]:
                    break
                self.backtracking(candidates, target - candidates[i], i+1, val+[candidates[i]]);
x = Solution()
print x.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)