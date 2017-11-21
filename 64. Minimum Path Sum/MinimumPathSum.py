class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        res = [[0 for i in range(col)] for j in range(row)]
        res[0][0] = grid[0][0]
        for i in range(1, row):
        	res[i][0] = res[i-1][0] + grid[i][0]
        for i in range(1, col):
        	res[0][i] = res[0][i-1] + grid[0][i]
        for i in range(1, row):
        	for j in range(1, col):
        		res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        return res[-1][-1]
print Solution().minPathSum([
	[1,3,1],
	[1,5,1],
	[4,2,1]
])