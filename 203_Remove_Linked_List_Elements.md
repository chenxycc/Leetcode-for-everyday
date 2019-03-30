```
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = cur = ListNode(-1)
        while head:
            if head.val != val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return dummy.next
```
