#### 法1

```
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
```
调试网站：http://www.pythontutor.com/live.html#mode=edit

#### 法2

> 指数排序
```
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in range(len(nums)):
            count[nums[i]] += 1
        for i in range(count[0]):
            nums[i] = 0
        for j in range(count[0], count[0] + count[1]):
            nums[j] = 1
        for k in range(count[0] + count[1], count[0] + count[1] + count[2]):
            nums[k] = 2
```
#### 法3

>三路快排

```
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, len(nums) - 1
        while one <= two:
            if nums[one] == 0:
                nums[zero], nums[one] =nums[one], nums[zero]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[one], nums[two] =nums[two], nums[one]
                two -= 1
```
