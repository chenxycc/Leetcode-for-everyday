```
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 节点为空，直接返回
        if node == None:
            return
        # 节点的下一节点为空，将当前设置为空
        if node.next == None:
            node = None
        # 将下一节点的值赋给该结点，并删除下一节点
        node.val = node.next.val
        delNode = node.next
        node.next = delNode.next 
```
