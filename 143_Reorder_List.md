1. 利用快慢指针找出中间节点，
2. 讲链表分成两个子链表
3. 反转后面的子链表
4. 合并两个子链表

```
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: 
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        head1, head2 = head, slow.next
        slow.next, cur, pre=None, head2, None
        while cur:
            curnext=cur.next
            cur.next=pre
            pre=cur
            cur=curnext
        cur1, cur2=head1, pre
        while cur2:
            next1, next2=cur1.next, cur2.next
            cur1.next=cur2
            cur2.next=next1
            cur1, cur2=next1, next2
```
