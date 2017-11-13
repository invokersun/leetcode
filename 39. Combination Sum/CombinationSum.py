class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.re = []
        self.backtracking(candidates,target,0,[])
        return Solution.re
    def backtracking(self, candidates, target, start, val):
        if target == 0:
            Solution.re.append(val)
        else:
            for i in range(start,len(candidates)):
                if target < 0:
                    break
                self.backtracking(candidates,target-candidates[i],i,val+[candidates[i]])
x = Solution()
print x.combinationSum([2,3,5,7], 7)