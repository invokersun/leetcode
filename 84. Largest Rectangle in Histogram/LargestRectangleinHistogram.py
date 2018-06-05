class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        i=0
        area=0
        while i<len(heights):
        	if stack==[] or heights[i]>heights[stack[len(stack)-1]]:
        		stack.append(i)
        	else:
        		curr=stack.pop()
        		width=i if stack==[] else i-stack[len(stack)-1]-1
        		area=max(area,width*heights[curr])
        		i-=1
        	i+=1
        while stack!=[]:
        	curr=stack.pop()
        	width=i if stack==[] else len(heights)-stack[len(stack)-1]-1
        	area=max(area,width*heights[curr])
        return area
print Solution().largestRectangleArea([2,1,5,6,2,3])