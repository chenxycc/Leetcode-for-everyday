### 方法与上题一样

```
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def arr(s):
            res = [1] *(len(s) + 1)
            for i in range(len(s) - 1):
                res[i+1] = s[i] + s[i+1]
            return res
        if rowIndex <0:
            return []
        elif rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            res = [1] * (rowIndex + 1)
            res[0], res[1] = [1], [1,1]
            for i in range(2, rowIndex+1):
                res[i] = arr(res[i-1])
            return res[-1]

```
