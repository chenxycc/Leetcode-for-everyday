### 依然采用二叉树层序遍历的方法

```
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view
```
