```
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        elif root.right:
            return 1 + self.minDepth(root.right)
        else:
            return 1
```
