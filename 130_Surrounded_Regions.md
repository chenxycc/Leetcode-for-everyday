### foolfill算法

```
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0]) if row else 0
        if not row:
            return
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 or i == row - 1 or j == col - 1:
                    if board[i][j] == "O":
                        self.mark(board, i, j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "*":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    def mark(self, board, i, j):
        row = len(board)
        col = len(board[0])
        if i<0 or j<0 or i>=row or j>=col or board[i][j] != 'O':
            return
        board[i][j] = "*"
        self.mark(board, i+1, j)
        self.mark(board, i-1, j)
        self.mark(board, i, j-1)
        self.mark(board, i, j+1)
```
