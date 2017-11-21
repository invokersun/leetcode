class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        res = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
        	if obstacleGrid[i][0] == 0:
        		res[i][0] = 1
        	else:
        		res[i][0] = 0
        		break
        for i in range(col):
        	if obstacleGrid[0][i]==0:
        		res[0][i] = 1
        	else:
        		res[0][i] = 0
        		break
        for i in range(1, row):
        	for j in range(1, col):
        		if obstacleGrid[i][j] == 1:
        			res[i][j] = 0
        		else:
        			res[i][j] = res[i][j-1] + res[i-1][j]
        return res[-1][-1]
print Solution().uniquePathsWithObstacles([
  [1, 0]
])