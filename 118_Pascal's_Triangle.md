### easy

```
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def arr(s):
            res = [1]*(len(s)+1)
            for i in range(len(s)-1):
                res[i+1] = s[i] +s[i+1]
            return res
        if numRows <= 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            res = [1]*numRows
            res[0], res[1] = [1], [1,1]
            for i in range(2, numRows):
                res[i] = arr(res[i-1])
            return res
```
