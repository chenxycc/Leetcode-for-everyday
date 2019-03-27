```
class Solution:
    def isHappy(self, n: int) -> bool:
        mem = []
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.append(n)
        else:
            return True
```
