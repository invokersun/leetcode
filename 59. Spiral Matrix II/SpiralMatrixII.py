class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        maxup=0
        maxleft=0
        maxright=n-1
        maxdown=n-1
        direction=0
        matrix=[[0 for i in range(n)] for j in range(n)]
        num=range(1,n*n+1)
        iter=0
        while True:
            if direction==0:
                for i in range(maxleft,maxright+1):
                    matrix[maxup][i]=num[iter]
                    iter+=1
                maxup+=1
            if direction==1:
                for i in range(maxup,maxdown+1):
                    matrix[i][maxright]=num[iter]
                    iter+=1
                maxright-=1
            if direction==2:
                for i in reversed(range(maxleft,maxright+1)):
                    matrix[maxdown][i]=num[iter]
                    iter+=1
                maxdown-=1
            if direction==3:
                for i in reversed(range(maxup,maxdown+1)):
                    matrix[i][maxleft]=num[iter]
                    iter+=1
                maxleft+=1
            if maxleft>maxright or maxup>maxdown:
                return matrix
            direction=(direction+1)%4
print Solution().generateMatrix(5)