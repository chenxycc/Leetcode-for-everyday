## 寻找中间值的位置，将链表且分为两段

```
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head :
            return head
        if  not head.next:
            return TreeNode(head.val)
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(dummy.next)
    
        return root
```
