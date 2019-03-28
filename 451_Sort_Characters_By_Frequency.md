```
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        res = str()
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        while len(dic) > 0:
            m = max(dic,key = dic.get)
            res += m * dic[m]
            del dic[m]
        return res
```
