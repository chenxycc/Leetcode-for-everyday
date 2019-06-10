```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.pre = None
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.pre
        root.left = None
        self.pre = root
```

- Runtime: 44 ms, faster than 79.68% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 13.2 MB, less than 84.87% of Python3 online submissions for Flatten Binary Tree to Linked List.
