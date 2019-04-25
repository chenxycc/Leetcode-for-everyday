```
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val+l2.val<10:
            l3 = ListNode(l1.val+l2.val)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            l3 = ListNode(l1.val+l2.val -10)
            temp = ListNode(1)
            l3.next = self.addTwoNumbers(l1.next,self.addTwoNumbers(l2.next,temp))
        return l3
 ```       
