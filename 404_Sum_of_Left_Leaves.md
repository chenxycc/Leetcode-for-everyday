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
