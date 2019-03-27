#### 滑动窗口

> 时间复杂度O(N)\
  空间复杂度O(1)

```
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r, sum, res = 0, -1, 0, len(nums) + 1
        while l < len(nums):
            if sum < s and r < len(nums) - 1:
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1
            if (sum >= s):
                res = min(res, r - l + 1)
        if res == len(nums) + 1:
            return 0
        return res
```
