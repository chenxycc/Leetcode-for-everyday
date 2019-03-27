```
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strlist = str.split(" ")
        if len(pattern) != len(strlist):
            return False
        lookup = {}
        for i in range(len(pattern)):
            if pattern[i] not in lookup:
                for key in lookup:
                    if lookup[key] == strlist[i]:
                        return False
                lookup[pattern[i]] = strlist[i]
            elif lookup[pattern[i]] != strlist[i]:
                return False
        return True
```
