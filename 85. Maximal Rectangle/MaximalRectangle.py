class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # if matrix == []:
        # 	return 0
        # heights=[0 for i in range(len(matrix[0]))]
        # maxArea=0
        # for i in range(len(matrix)):
        # 	for j in range(len(matrix[i])):
        # 		heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
        # 	stack=[]
	       #  i=0
	       #  area=0
	       #  while i<len(heights):
	       #  	if stack==[] or heights[i]>heights[stack[len(stack)-1]]:
	       #  		stack.append(i)
	       #  	else:
	       #  		curr=stack.pop()
	       #  		width=i if stack==[] else i-stack[len(stack)-1]-1
	       #  		area=max(area,width*heights[curr])
	       #  		i-=1
	       #  	i+=1
	       #  while stack!=[]:
	       #  	curr=stack.pop()
	       #  	width=i if stack==[] else len(heights)-stack[len(stack)-1]-1
	       #  	area=max(area,width*heights[curr])
        # 	maxArea = max(maxArea, area)
        # return maxArea
        
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in xrange(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in xrange(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
print Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])