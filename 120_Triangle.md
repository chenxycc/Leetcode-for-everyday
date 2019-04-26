### 经典的动态规划问题

> 调试过程使用 http://www.pythontutor.com/live.html#mode=edit
```
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle) == 0:
            return 0
        dp = []
        for i in range(len(triangle)):
            dp.append(triangle[i])
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])

```
