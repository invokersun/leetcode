class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = [False for i in range(m)]
        colum = [False for j in range(n)]

        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			row[i] = True
        			colum[j] = True

        for i in range(m):
        	for j in range(n):
        		if row[i] or colum[j]:
        			matrix[i][j] = 0