### 数组转平衡BST：递归

```
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        root = TreeNode(nums[len(nums)//2])
        root.left = self.sortedArrayToBST(nums[:len(nums)//2])
        root.right = self.sortedArrayToBST(nums[len(nums)//2 + 1:])
        return root
```
