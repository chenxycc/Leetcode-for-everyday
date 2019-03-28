```
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False
        dicts = collections.OrderedDict()

        for i in range(len(nums)):
            key = nums[i] // max(1,t)
            for m in (key - 1,key,key + 1):
                if m in dicts and abs(nums[i] - dicts[m]) <= t:
                    return True
            dicts[key] = nums[i]
            if i >= k:
                dicts.popitem(last = False)
        return False
```
