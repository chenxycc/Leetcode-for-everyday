### 1:暴力

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_money = 0
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > max_money:
                    max_money = prices[j] - prices[i]
        return max_money
```

- 超时了

### 2：
