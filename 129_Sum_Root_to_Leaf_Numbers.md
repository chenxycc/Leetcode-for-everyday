```
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node, path):
            if node and not node.left and not node.right:
                self.res += int(''.join(str(i) for i in path+[node.val]))
            else:
                if node.left:
                    helper(node.left, path+[node.val])
                if node.right:
                    helper(node.right, path+[node.val])
        if not root:
            return 0
        helper(root, [])
        return self.res
```
