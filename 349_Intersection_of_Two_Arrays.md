```
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1
        for i in nums2:
            if i in map and map[i] > 0:
                res.append(i)
                map[i] = 0
        return res
```
