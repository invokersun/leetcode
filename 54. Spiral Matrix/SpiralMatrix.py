class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
        	return []
        res = []
        direction = 0
        up = left = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        while up <= down and left <= right:
        	if direction == 0:
        		for i in range(left,right + 1):
        			res.append(matrix[up][i])
        		up += 1
        	elif direction == 1:
        		for i in range(up,down + 1):
        			res.append(matrix[i][right])
        		right -= 1
        	elif direction == 2:
        		for i in range(left,right + 1)[::-1]:
        			res.append(matrix[down][i])
        		down -= 1
        	else:
        		for i in range(up,down + 1)[::-1]:
        			res.append(matrix[i][left])
        		left += 1
        	direction = (direction+1)%4
        return res
print Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])