####  滑动窗口

```
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, 0
        res, map = [], {}
        for c in p:
            map[c] = map.get(c, 0) + 1
        count = len(map)
        while r < len(s):
            if s[r] in map:
                map[s[r]] -= 1
                if map[s[r]] == 0:
                    count -= 1
            r += 1
            while count == 0:
                if r - l == len(p):
                    res.append(l)
                if s[l] in map:
                    map[s[l]] += 1
                    if map[s[l]] == 1:
                        count += 1
                l += 1                
        return res
```
