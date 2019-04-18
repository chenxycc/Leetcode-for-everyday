### 简单方法

- 先将BST转换为有序数组
- 直接输入Kth

```
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.lis = []
        self.root = root
        self.inorder(root)
        return self.lis[k-1]
    def inorder(self, root):
        if root == None:
            return 
        self.inorder(root.left)
        self.lis.append(root.val)
        self.inorder(root.right)
```

### 递归

- 扫root的左子树看nodes量
- 如果nodes数量是k-1，那么root就刚好是第k个
- 如果大于k > 左子树数量，扫右子树，同时更新root为root.right。

```
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def count(node):
            if not node:
                return 0
            return count(node.left) + count(node.right) + 1
        if not root:
            return None
        left = count(root.left)
        if left == k - 1:
            return root.val
        elif left > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - left - 1)
```
