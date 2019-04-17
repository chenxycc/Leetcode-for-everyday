```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, maps, buckets = [], collections.Counter(nums), ["*"] * (len(nums) + 1)
        for key in maps:
            if buckets[maps.get(key)] == "*":
                buckets[maps.get(key)] = []
            buckets[maps.get(key)].append(key)
        i = len(nums)
        while len(res) < k and i >= 0:
            if buckets[i] != "*":
                res.extend(buckets[i])
            i -= 1
        return res
```
