class Solution(object):
    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
        	for j, col in enumerate(row):
        		if col != '.':
        			seen += [(col, j), (i, col), (i/3, j/3, col)]
        return len(seen) == len(set(seen))

    def isValidSudoku2(self, board):
    	for i in range(9):
            if not self.isValidNine(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.isValidNine(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]
                if not self.isValidNine(block):
                    return False
        return True

    def isValidNine(self, row):
        map = {}
        for c in row:
            if c != '.':
                if c in map:
                    return False
                else:
                    map[c] = True
        return True
x = Solution()
board = [
"53..7....",
"6..195...",
".98....6.",
"8...6...3",
"4..8.3..1",
"7...2...6",
".6....28.",
"...419..5",
"....8..79"
]
#print x.isValidSudoku1(board)
print x.isValidSudoku2(board)