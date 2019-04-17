### 递归
- 判断左右子树最大高度差不超过1且左右子树均为平衡树

```
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

```
