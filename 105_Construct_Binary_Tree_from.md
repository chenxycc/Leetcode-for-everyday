### 回溯法

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
```

> Runtime: 136 ms, faster than 71.74% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 52.1 MB, less than 63.59% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
