### 法1：直接使用102题的解法

```
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res, que = [], [root]
        while root and que:
            res.append([node.val for node in que])
            LRpair = [(node.left, node.right) for node in que]
            que = [leaf for LR in LRpair for leaf in LR if leaf]
        return res[::-1]
```

### 法2：

```

```
