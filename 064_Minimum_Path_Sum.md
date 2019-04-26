### Solution1:

```
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        
        dp = [[grid[i][j] for j in range(col)] for i in range(row)]
        
        for i in range(1, col):
            dp[0][i] += dp[0][i-1]
        for i in range(1, row):
            dp[i][0] += dp[i-1][0]
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
```
### Solution2:

```
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        
        #dp = [[grid[i][j] for j in range(col)] for i in range(row)]
        
        for i in range(1, col):
            grid[0][i] += grid[0][i-1]
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
```
