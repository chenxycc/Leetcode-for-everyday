### floodfill算法

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.sink(i, j, grid)
                    count += 1
        return count
    def sink(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = "*"
        self.sink(i+1, j, grid)
        self.sink(i-1, j, grid)
        self.sink(i, j-1, grid)
        self.sink(i, j+1, grid)

```
