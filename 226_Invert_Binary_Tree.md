### Google面试题：递归

```
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return 
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```
