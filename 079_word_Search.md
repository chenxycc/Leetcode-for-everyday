### 方法1

```
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0:# all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j] # first character is found, check the remaining part
        board[i][j] = "#" # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
```

### 方法2

```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True
        row = len(board)
        col = len(board[0]) if row else 0

        def dfs(i, j, idx):
            if not 0 <= i <= row - 1 or not 0 <= j <= col - 1 or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[i][j] = "*"
            res = dfs(i + 1, j, idx + 1) or dfs(i, j + 1, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j - 1, idx + 1)
            board[i][j] = word[idx]
            return res
        
        return any(dfs(i, j, 0) for i in range(row) for j in range(col))
```

> -  √ 87/87 cases passed (232 ms)
> -  √ Your runtime beats 75.77 % of python3 submissions
> -  √ Your memory usage beats 23.42 % of python3 submissions (14.1 MB) 
