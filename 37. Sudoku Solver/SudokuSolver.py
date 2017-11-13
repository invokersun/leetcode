class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
    def valid(self, x, y, board):
        tmp = board[x][y]
        board[x][y] = '.'
        for row in range(9):
            if board[row][y] == tmp:
                return False
        for col in range(9):
            if board[x][col] == tmp:
                return False
        for row in range(3):
            for col in range(3):
                if board[(x / 3) * 3 + row][(y / 3) * 3 + col] == tmp:
                    return False
        board[x][y] = tmp
        return True
    def dfs(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        board[row][col] = char
                        if self.valid(row, col, board) and self.dfs(board):
                            return True
                        board[row][col] = '.'
                    return False
        return True
x = Solution()
board = [
[".",".","9","7","4","8",".",".","."],
["7",".",".",".",".",".",".",".","."],
[".","2",".","1",".","9",".",".","."],
[".",".","7",".",".",".","2","4","."],
[".","6","4",".","1",".","5","9","."],
[".","9","8",".",".",".","3",".","."],
[".",".",".","8",".","3",".","2","."],
[".",".",".",".",".",".",".",".","6"],
[".",".",".","2","7","5","9",".","."]
]
print x.solveSudoku(board)