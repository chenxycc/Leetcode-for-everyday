```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        for i in nums:
            if i != 0:
                res.append(i)
        for i in range(len(res)):
            nums[i] = res[i]
        for i in range(len(res), len(nums), 1):
            nums[i] = 0
```

> 方法2
不需要额外的内存

```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0
```
