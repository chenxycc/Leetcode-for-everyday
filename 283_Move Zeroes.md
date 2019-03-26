#### 法1

>时间复杂度O(N)
空间复杂度O(N)
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

#### 法2

不需要额外的内存
> 时间复杂度O(N)
空间复杂度O(1)
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
#### 法3

> 不再需要赋值操作，直接将0元素移动到数组尾部
```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
```

#### 法4

> 法3存在问题：当所有元素都为0，还需要进行交换
```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(0, len(nums), 1):
            if nums[i] != 0:
                if i != k:
                    nums[k], nums[i] = nums[i], nums[k]
                k += 1
```
