class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmostheigh = [0 for i in range(len(height))]
        leftmax = 0
        for i in range(len(height)):
        	if height[i] > leftmax:
        		leftmax = height[i]
        	leftmostheigh[i] = leftmax
        sum = 0
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax:
            	rightmax = height[i]
            if min(rightmax, leftmostheigh[i]) > height[i]:
                sum += min(rightmax, leftmostheigh[i]) - height[i]
        return sum
x = Solution()
print x.trap([0,1,0,2,1,0,1,3,2,1,2,1])