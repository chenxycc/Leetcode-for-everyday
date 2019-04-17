### 法1：直接递归

```
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```
> Your runtime beats 14.06 % of python3 submissions

### 法2：利用特性

> complete binary tree的特性是除了最后一层，之前的就是perfect tree. 所以寻找左子树的最左边的高度left_most_height\
和右子树的最右边的node高度right_most_height，如果相同就是perfect tree，高度2^h - 1， 否则递归的来看左子树和右子树

```
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if  not root:
            return 0
        p, q = root, root
        lmh, rmh = 0, 0
        while p:
            p = p.left
            lmh +=  1
        while q:
            q = q.right
            rmh += 1
        if lmh == rmh:
            return 2 ** lmh - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

```

> Your runtime beats 89.75 % of python3 submissions
