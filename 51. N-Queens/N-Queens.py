class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isqueens(depth, val):
        	for i in range(depth):
        		if board[i] == val or abs(depth-i) == abs(board[i]-val):
        			return False
        	return True
        def dfs(depth, row):
        	if depth == n:
        		ans.append(row)
        		return
        	for i in range(n):
        		if isqueens(depth, i):
        			board[depth] = i
        			dfs(depth+1, row+['.'*i + 'Q' + '.'*(n-1-i)])
        board = [-1 for i in range(n)]
        ans = []
        dfs(0, [])
        return ans
print Solution().solveNQueens(4)