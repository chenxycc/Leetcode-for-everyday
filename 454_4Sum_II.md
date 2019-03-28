```
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = {}
        for i in A:
            for j in B:
                if i+j not in dic:
                    dic[i+j] = 1
                else:
                    dic[i+j] += 1
        res = 0
        for i in range(len(C)):
            for j in range(len(D)):
                if 0 - C[i] - D[j] in dic:
                    res += dic[0 - C[i] - D[j]]
        return res
```
