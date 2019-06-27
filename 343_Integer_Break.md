### 直接递归
```
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 1:
            return 1
        res = -1
        for i in range(1,n):
            res = max(res, i * (n-i), i * self.integerBreak(n - i))
        return res
        
```

- ~_~超时了

### 记忆话搜索
```
class Solution:    
    def integerBreak(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def help(n):
            if n == 1:
                return 1
            res = -1
            if memo[n] != -1:
                return memo[n]
            for i in range(1,n):
                res = max(res, i * (n-i), i * help(n - i))
            memo[n] = res
            return res
        
        
        return help(n)
```
- Runtime: 32 ms, faster than 92.09% of Python3 online submissions for Integer Break.
Memory Usage: 13.1 MB, less than 80.05% of Python3 online submissions for Integer Break.
