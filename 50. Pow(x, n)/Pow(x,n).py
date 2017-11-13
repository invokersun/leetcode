class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:  
            return 1  
        if n<0:  
            return 1.0/self.myPow(x,-n)  
        if n%2==1:  
            return x*self.myPow(x*x,n/2)  
        else:  
            return self.myPow(x*x,n/2)
print Solution().myPow(2, 5)