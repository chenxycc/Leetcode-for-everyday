### 典型递归

- 检查root的左孩子是不是leaf node，是的话加上它的值，不是的话递归去求它的孩子们的，对于右边，递归的求sum of left leaves

```
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def isleaf(node):
            if not node:
                return False
            if not node.left and not node.right:
                return True
            return False
        res = 0
        if root:
            if isleaf(root.left):
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)
            res += self.sumOfLeftLeaves(root.right)
        return res
```
