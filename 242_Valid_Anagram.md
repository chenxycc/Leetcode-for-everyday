```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        maps = {}
        for i in s:
            maps[i] = maps[i] + 1 if i in maps else 1
        for i in t:
            if i in maps:
                maps[i] -= 1
        for i in maps:
            if maps[i] != 0:
                return False
        return True
```
