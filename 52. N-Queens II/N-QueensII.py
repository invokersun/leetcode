class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isqueens(depth, val):
        	for i in range(depth):
        		if board[i] == val or abs(depth-i) == abs(board[i]-val):
        			return False
        	return True
        def dfs(depth):
        	if depth == n:
        		ans.append(0)
        		return
        	for i in range(n):
        		if isqueens(depth, i):
        			board[depth] = i
        			dfs(depth+1)
        board = [-1 for i in range(n)]
        ans = []
        dfs(0)
        return len(ans)
print Solution().totalNQueens(4)