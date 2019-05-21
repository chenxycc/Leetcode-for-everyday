### 依然回溯

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])
        root.right = self.buildTree(inorder[ind+1:], postorder)
        root.left = self.buildTree(inorder[:ind], postorder)
        return root

```

> Runtime: 132 ms, faster than 71.78% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 52.1 MB, less than 65.09% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
